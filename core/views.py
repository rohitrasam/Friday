from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from .models import *

import requests
from bs4 import BeautifulSoup
# Create your views here.

URL = 'https://edurank.org/geo/in/'
BASE_URL = URL[:URL.find('/g')]

@api_view(['GET'])
def upload_to_db(request: Request) -> Response:
    """
        Scrapes academic fields and branches from website and inserts into database
    """

    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")

    scripts = soup.find_all('script')[-2].text
    start_idx = scripts.find('[')
    fields = eval(scripts[start_idx:])

    country, _ = Country.objects.get_or_create(name="India")

    try:
        for field, field_site, branches in fields:
            
            if field_site == "":
                field_site = URL
            else:
                field_site = BASE_URL+field_site

            page = requests.get(field_site)
            soup = BeautifulSoup(page.text, "html.parser")
            
            
            # Get field from field or create field in field table if not already existing
            field, _ = AcademicField.objects.get_or_create(name=field)
            colleges_elem = soup.find_all('div', class_='block-cont pt-4 mb-4')
            for college in colleges_elem:
                rank, name = college.find('h2').text.strip().split(". ", 1)
                college, _ = College.objects.get_or_create(name=name, country_code=country)
                FieldRank.objects.create(college=college, field=field, rank=rank)


            for branch in branches:
                if branch[1].endswith("in/"):
                    branch[1] = BASE_URL + branch[1]
                else:
                    continue
                page = requests.get(branch[1])
                soup = BeautifulSoup(page.text, 'html.parser')
                branch,  _ = AcademicBranch.objects.get_or_create(name=branch[0], field=field)
                colleges_elem = soup.find_all('div', class_='block-cont pt-4 mb-4')
                for college in colleges_elem:
                    rank, name = college.find('h2').text.strip().split(". ", 1)
                    college, _ = College.objects.get_or_create(name=name, country_code=country)
                    BranchRank.objects.create(college=college, branch=branch, rank=rank)

        return Response(data=fields, status=status.HTTP_200_OK)
    except:
        return Response(data="Could not insert into db", status=status.HTTP_400_BAD_REQUEST)
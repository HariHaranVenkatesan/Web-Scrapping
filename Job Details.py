from bs4 import BeautifulSoup
import requests
import time
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Timesjos'
print(excel.sheetnames)
sheet.append(['company name','required skills','more info'])


print("Enter the skills that you know")
familiar_skills = input('>')
print("Filtering Out")


#def find_jobs():
html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
html.raise_for_status()
soup = BeautifulSoup(html.text, "lxml")
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for index, job in enumerate(jobs):
    published_date = job.find('span', class_="sim-posted").span.text
    if "few" in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if familiar_skills in skills:
        sheet.append([company_name, skills, more_info])
            print(f"Company_name:{company_name.strip()}")
            print(f"Required skills :{skills.strip()}")
            print(f"More Info : {more_info}")
excel.save('Jobs Details.xlsx')




#if '__main__' == __name__:
    #find_jobs()
       # time_wait = 2
       # print(f'waiting {time_wait} minutes....')
       # time.sleep(time_wait * 60)


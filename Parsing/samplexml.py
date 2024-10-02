import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()
Job_Title = []
Company = []
Category = []
City = []

for title in root.iter('job_title'):
    Job_Title.append(title.text)

for company in root.iter('company'):
    Company.append(company.text)

for category in root.iter('category'):
    Category.append(category.text)

for city in root.iter('city'):
    City.append(city.text)

print(Job_Title)
print(Company)
print(Category)
print(City)
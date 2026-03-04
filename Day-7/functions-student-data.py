def student_data(info):
    print(f'Name:{info[0]}\nCourse:{info[1]}\nGra_year:{info[2]}')

data=[['Pooja','PFS','2024'],
      ['Keerthi','DA','2026'],
      ['Teju','PFS','2025'],
      ['Dheeru','JFS','2024'],
      ]
for i in data:
    student_data(i)

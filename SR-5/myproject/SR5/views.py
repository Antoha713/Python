from django.http import HttpResponse

def profile_table(request):
    name = "Жилик Анна"
    email = "st7314617@stud.duikt.edu.ua"
    city = "Київ"
    occupation = "Студентка"
    hobby = "Dota 2"

    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="utf-8">
        <title>Моя інформація</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f9f9f9; padding: 40px; }}
            table {{ border-collapse: collapse; width: 50%; background: white; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #999; padding: 8px 12px; text-align: left; }}
            th {{ background-color: #e0e0e0; }}
            caption {{ font-weight: bold; margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <table>
            <caption>Інформація про мене</caption>
            <tr><th>Поле</th><th>Значення</th></tr>
            <tr><td>Ім'я</td><td>{name}</td></tr>
            <tr><td>Email</td><td>{email}</td></tr>
            <tr><td>Місто</td><td>{city}</td></tr>
            <tr><td>Професія</td><td>{occupation}</td></tr>
            <tr><td>Хобі</td><td>{hobby}</td></tr>
        </table>
    </body>
    </html>
    """

    return HttpResponse(html)

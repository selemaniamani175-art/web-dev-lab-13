from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Online Examination Management System</title>
    </head>

    <body>

        <h1>ONLINE EXAMINATION MANAGEMENT SYSTEM</h1>

        <hr>

        <h2>Welcome</h2>

        <p>This is an Online Examination Management System developed using Django.</p>

        <hr>

        <h3>Navigation</h3>

        <ul>
            <li><a href="/students/">Students</a></li>
            <li><a href="/exams/">Exams</a></li>
            <li><a href="/results/">Results</a></li>
            <li><a href="/admin/">Admin Dashboard</a></li>
        </ul>

    </body>
    </html>
    """)
<html>
<head>
<title>Index síða</title>

</head>
<body>
    
    <h1>Kennitölur</h1>
    <a href="/">Home</a>
    {% for x in nofn %}
        <h3>{{x[0]}} <a href="/{{ x[1] }}">{{ x[1] }}</a></h3>
    {% endfor %}
  

</body>
</html>
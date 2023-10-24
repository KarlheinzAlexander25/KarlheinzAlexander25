
{
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Personal Portfolio Website</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>

    <div class="hero">
        <nav>
            <img src="{% static 'img/logo.png' %}" class="logo">
            <ul>
                <li><a href="{% url 'home' %}">Home</a></li>
                <li><a href="{% url 'about' %}">About</a></li>
                <li><a href="{% url 'service' %}">Service</a></li>
                <li><a href="{% url 'portfolio' %}">Portfolio</a></li>
                <li><a href="{% url 'blog' %}">Blog</a></li>
                <li><a href="{% url 'contact' %}">Contact</a></li>
            </ul>
            <a href="#" class="btn">Buy Now</a>
        </nav>

        <div class="content">
            <span class="title">Freelance Web Developer</span>
            <h1>Hello, I’m <span>Alexander</span></h1>
            <p>I’m working on a professional, visually sophisticated and technologically proficient, responsive and multi-functional React Template Imroz.</p>
            <a href="#" class="btn">Download CV</a>
        </div>
    </div>

</body>
</html>
    }
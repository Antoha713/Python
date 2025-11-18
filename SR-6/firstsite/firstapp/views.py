from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .data import BloggersData


def wrap(content):
    return HttpResponse(f"<html><body>{content}</body></html>")


def home(request):
    html = """
        <h1>Головна сторінка</h1>
        <table border='1' cellpadding='5'>
            <tr><th><a href='/news/'>Новини</a></th></tr>
        </table>
        <br><a href='/profiles/'>Перейти до профілів</a>
    """
    return wrap(html)


def profiles(request):
    rows = "".join([
        f"<tr><td><a href='/profiles/{id}/'>{data['name']}</a></td>"
        f"<td>{data['category']}</td><td>{data['description']}</td></tr>"
        for id, data in BloggersData.bloggers.items()
    ])

    html = f"""
        <h1>Профілі блогерів</h1>
        <table border='1' cellpadding='5'>
            <tr><th>Ім'я</th><th>Категорія</th><th>Опис</th></tr>
            {rows}
        </table>
        <br><a href='/'>На головну</a>
    """
    return wrap(html)


def profile_details(request, blogger_id):
    blogger_id = int(blogger_id)
    data = BloggersData.bloggers.get(blogger_id)

    if not data:
        return HttpResponseNotFound("<h1>404 — Блогера не знайдено</h1>")

    posts = "".join([f"<li>{p}</li>" for p in data['posts']])

    html = f"""
        <h1>Профіль: {data['name']}</h1>
        <table border='1' cellpadding='5'>
            <tr><td>Категорія</td><td>{data['category']}</td></tr>
            <tr><td>Опис</td><td>{data['description']}</td></tr>
            <tr><td>Соцмережа</td><td><a href='{data['social']}'>Перейти</a></td></tr>
        </table>
        <h3>Останні публікації:</h3>
        <ul>{posts}</ul>
        <br><a href='/profiles/'>Назад до списку</a>
    """
    return wrap(html)

def news(request):
    html = """
        <h1>Останні новини зі світу блогерів</h1>
        <table border='1' cellpadding='5'>
            <tr><th>Новина</th><th>Дата</th></tr>
            <tr><td>bloger1 запустив новий курс з AI</td><td>2025-01-12</td></tr>
            <tr><td>bloger2 випустив книгу рецептів</td><td>2025-01-10</td></tr>
            <tr><td>Нова платформа для блогерів — InfluencerHub</td><td>2025-01-09</td></tr>
        </table>
        <br><a href='/'>На головну</a>
    """
    return HttpResponse(html)



def redirect_to_home(request):
    return HttpResponseRedirect(reverse('home'))

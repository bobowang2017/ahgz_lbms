from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        sql = 'CREATE DATABASE world'
        cursor = connection.cursor()
        cursor.execute(sql)
        print('create database success')
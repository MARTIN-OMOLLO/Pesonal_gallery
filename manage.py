import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_gallery.settings')
    try:
     from django.core.management import execute_from_command_line
    

if __name__ == '__main__':
    main()
    

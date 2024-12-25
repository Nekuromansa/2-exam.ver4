django-blog/
│
├── articles/            # Postlar va kommentariylarni boshqarish uchun ilova
│   ├── migrations/      # Ma'lumotlar bazasining migratsiyalari
│   ├── models.py        # Maqolalar uchun modellar
│   ├── views.py         # Maqolalarni ko'rsatish uchun views
│   └── urls.py          # Blog uchun yo'llar
│
├── config/              # Django loyihasining asosiy qismlari
│   ├── settings.py      # Loyiha sozlamalari
│   ├── urls.py          # Loyiha uchun asosiy yo'llar
│   └── wsgi.py          # WSGI konfiguratsiyasi
│
└── manage.py            # Loyiha boshqaruv fayli

# Loyiha ishga tushishi uchun : "python manage.py runserver"
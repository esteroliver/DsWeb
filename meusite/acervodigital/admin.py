from django.contrib import admin
from .models import Usuario, Contato, Emprestimo, Livro

admin.site.register(Usuario)
admin.site.register(Contato)
admin.site.register(Emprestimo)
admin.site.register(Livro)

from django.contrib import admin

# Register your models here.
from hw3app.models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    ordering = ['name', 'email', '-created']
    list_filter = ['address']
    search_fields = ['name', 'email']
    search_help_text = 'Поиск по имени или почте'

    readonly_fields = ['created']
    fieldsets = [
        ('Имя клиента', {
            'classes': 'wide',
            'fields': ['name']
        }),
        ('Контакты', {
            'fields': ['email', 'phone']
        }),
        ('Адрес', {
            'fields': ['address']
        }),
        (None, {
            'fields': ['created']
        }),
    ]


class ProdsOrder(admin.TabularInline):
    model = Order.products.through
    verbose_name = 'Продукты в заказе'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount']  # отображение списка продуктов
    ordering = ['name', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_amount]          # Добавление операций над продуктами
    inlines = [ProdsOrder]

    # Настройка формы для редактировании отдельного продукта
    # fields = ['name', 'description', 'price', 'amount', 'created']   # fields or fieldsets
    readonly_fields = ['created']
    fieldsets = [                              # Разделение на логические секции
        ('Название продутка', {                               # Заголовок секции
                'classes': ['wide'],           # Поле развернуто
                'fields': ['name'], },
         ),
        ('Подробности', {
                 'classes': ['collapse'],      # Поле свернуто
                 'description': 'Подробное описание',
                 'fields':['description'], },
         ),
        ('Бухгалтерия', {
                 'fields': ['price', 'amount'], }
         ),
        (None, {
                 'description': 'Дата добавление продукта в базу',
                 'fields': ['created'], }
         ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'get_products_names', 'get_total_price', 'created']

    readonly_fields = ['client_id', 'created', 'get_total_price']
    inlines = (ProdsOrder,)
    exclude = ('products', 'total_price')
    fieldsets = [
        ('Имя Клиента', {
            'fields': ['client_id']
        }),
        ('Дата создания заказа', {
            'fields': ['created']
        }),
        ('Итого', {
            'fields': ['get_total_price']
        })
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

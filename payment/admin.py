from django.contrib import admin
from .models import Payment, TypePlan

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'method', 'amount', 'status', 'created_at')
    list_filter = ('user', 'type', 'method', 'status')
    search_fields = ('user__username', 'type', 'method', 'amount', 'status')
    readonly_fields = ('user',)  # Fields that should be read-only in the admin
    

@admin.register(TypePlan)
class TypePlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'duration', 'is_active', 'is_default')
    list_filter = ('is_active', 'is_default')
    search_fields = ('name', 'description', 'price', 'duration', 'is_active', 'is_default')    
    
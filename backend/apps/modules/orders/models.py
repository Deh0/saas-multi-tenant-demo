from django.db import models
from django.utils.translation import gettext_lazy as _

class Cart(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="carts",
        verbose_name=_("Usuário")
    )
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Carrinho #{self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Carrinho")
    )
    product = models.ForeignKey(
        "catalog.Product", 
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name=_("Produto")
    )
    product_variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.SET_NULL,
        related_name="cart_items",
        verbose_name=_("Variação do Produto"),
        blank=True,
        null=True
    )
    quantity = models.PositiveIntegerField(_("Quantidade"), default=1)
    unit_price = models.DecimalField(_("Preço Unitário"), max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(_("Subtotal"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f" {self.product.name}"
    
class Order(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("Usuário")
    )
    delivery_address = models.ForeignKey(
        "users.Address",
        on_delete=models.SET_NULL,
        related_name="orders",
        verbose_name=_("Endereço de Entrega"),
        blank=True,
        null=True
    )
    # cupom id (FK) ainda preciso criar

    status = models.CharField(_("Status"), max_length=20, default="pending")
    subtotal_price = models.DecimalField(_("Preço Subtotal"), max_digits=10, decimal_places=2)
    freight_value = models.DecimalField(_("Valor do Frete"), max_digits=10, decimal_places=2)
    discount_value = models.DecimalField(_("Valor do Desconto"), max_digits=10, decimal_places=2)
    total_price = models.DecimalField(_("Preço Total"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.user.name} {self.user.surname}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Pedido")
    )
    product = models.ForeignKey(
        "catalog.Product", 
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("Produto")
    )
    product_variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.SET_NULL,
        related_name="order_items",
        verbose_name=_("Variação do Produto"),
        blank=True,
        null=True
    )
    quantity = models.PositiveIntegerField(_("Quantidade"), default=1)
    unit_price = models.DecimalField(_("Preço Unitário"), max_digits=10, decimal_places=2)
    discount_value = models.DecimalField(_("Valor do Desconto"), max_digits=10, decimal_places=2)
    product_name_snapshot = models.CharField(_("Nome do Produto (Snapshot)"), max_length=255)
    variant_snapshot = models.CharField(_("Variação do Produto (Snapshot)"), max_length=255, blank=True, null=True)
    subtotal = models.DecimalField(_("Subtotal"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f" {self.product.name}"

class OrderHistory(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name="history",
        verbose_name=_("Pedido")
    )
    status = models.CharField(_("Status"), max_length=20)
    changed_at = models.DateTimeField(_("Alterado em"), auto_now_add=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
    
    def __str__(self):
        return f"Histórico do Pedido #{self.order.id} - {self.status} em {self.changed_at}"
    

from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    tenant = models.ForeignKey(
        "tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name=_("Empresa")
    )
    name = models.CharField(_("Nome"), max_length=255)
    description = models.TextField(_("Descrição"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.name
    
class Collection(models.Model):
    tenant = models.ForeignKey(
        "tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name=_("Empresa")
    )
    name = models.CharField(_("Nome"), max_length=255)
    description = models.TextField(_("Descrição"), blank=True, null=True)
    start_date = models.DateField(_("Data de Início"), blank=True, null=True)
    end_date = models.DateField(_("Data de Término"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    tenant = models.ForeignKey(
        "tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("Empresa")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name=_("Categoria"),
        blank=True,
        null=True
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name=_("Coleção"),
        blank=True,
        null=True
    )
    name = models.CharField(_("Nome"), max_length=255)
    sku = models.CharField(_("SKU"), max_length=50, unique=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    short_description = models.CharField(_("Descrição Curta"), max_length=255, blank=True, null=True)
    price = models.DecimalField(_("Preço"), max_digits=10, decimal_places=2)
    base_cost = models.DecimalField(_("Custo Base"), max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(_("Peso"), max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
        verbose_name=_("Produto")
    )
    sku = models.CharField(_("SKU"), max_length=50, unique=True)
    color = models.CharField(_("Cor"), max_length=50, blank=True, null=True)
    size = models.CharField(_("Tamanho"), max_length=50, blank=True, null=True)
    price_override = models.DecimalField(_("Preço Adicional"), max_digits=10, decimal_places=2, default=0)
    status = models.CharField(_("Status"), max_length=20, default="active")
    stock_quantity = models.PositiveIntegerField(_("Quantidade em Estoque"), default=0)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"
    
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Produto")
    )
    image_url = models.URLField(_("URL da Imagem"))
    alt_text = models.CharField(_("Texto Alternativo"), max_length=255, blank=True, null=True)
    is_primary = models.BooleanField(_("Imagem Principal"), default=False)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Imagem do {self.product.name}"
    
# Adicionar campo para atributo, uma classe de atributo e outra de produto atributo
class ProductDetail(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="details",
        verbose_name=_("Detalhes produto")
    )
    full_description = models.CharField(_("Descrição Completa"), max_length=255)
    material = models.CharField(_("Material"), max_length=255, blank=True, null=True)
    origin = models.CharField(_("Origem"), max_length=255, blank=True, null=True)
    weight = models.DecimalField(_("Peso"), max_digits=10, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(_("Altura"), max_digits=10, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(_("Largura"), max_digits=10, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(_("Comprimento"), max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Detalhes de {self.product.name}"
    
class Favorite(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name=_('Usuário')
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name=_('Produto')
    )
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)
    
    class Meta:
        verbose_name = _('Favorito')
        verbose_name_plural = _('Favoritos')
        unique_together = ('user', 'product')
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
    
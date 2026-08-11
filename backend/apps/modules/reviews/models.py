from django.db import models
from django.utils.translation import gettext_lazy as _

class Review(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Usuário')
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Produto')
    )
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Pedido')
    )
    RATING = [
        (1, _('1 estrela')),
        (2, _('2 estrelas')),
        (3, _('3 estrelas')),
        (4, _('4 estrelas')),
        (5, _('5 estrelas')),
    ]
    rating = models.PositiveIntegerField(_('Avaliação'), choices=RATING, default=5)
    title = models.CharField(_('Título'), max_length=100)
    comment = models.TextField(_('Comentário'), blank=True)
    status = models.CharField(_('Status'), max_length=20, default='pending')
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Avaliação')
        verbose_name_plural = _('Avaliações')
    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.rating} estrelas'
    
class ReviewImage(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Avaliação')
    )
    image_url = models.URLField(_('URL da Imagem'))
    status = models.CharField(_('Status'), max_length=20, default='pending')
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Imagem de Avaliação')
        verbose_name_plural = _('Imagens de Avaliações')
    def __str__(self):
        return f'{self.review.user.username} - {self.review.product.name} - Imagem'
    
from django.db.models import signals
from django.dispatch import dispatcher

def count_animales(sender, instance, signal, *args, **kwargs):
  """
  Runs through all the change types and adds up their current numbers
  """
  print instance
  from models import Lote
  for lote in Lote.objects.filter(establecimiento=instance.establecimiento):
    lote.count_animales()
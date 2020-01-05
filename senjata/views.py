from django.views.generic import TemplateView,ListView
from pinjam.views import ListSenjata

class IndexView(TemplateView,ListSenjata):
	"""docstring for """

	template_name = 'index.html'

	def get_context_data(self):
		context = self.get_list_senjata_perkategori()
		return context

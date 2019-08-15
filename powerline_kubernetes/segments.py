# vim:fileencoding=utf-8:noet
from powerline.segments import Segment, with_docstring
from kubernetes import config
import os

class KubernetesSegment(Segment):

	def build_segments(self, context, namespace=None):
		segments = [
			{
				'contents'               : u'\U00002388 ', 'highlight_groups': ['kubernetes'],
				'divider_highlight_group': 'kubernetes:divider'
			},
		]
		if namespace:
			segments.append(
					{
						'contents'               : '%s - %s' % (context, namespace), 'highlight_groups': [
						'kubernetes'],
						'divider_highlight_group': 'kubernetes:divider'
					}
			)
		else:
			segments.append(
					{
						'contents'               : '%s' % context, 'highlight_groups': ['kubernetes'],
						'divider_highlight_group': 'kubernetes:divider'
					}
			)

		return segments

	def __call__(self, pl):
		pl.debug('Running powerline-kubernetes')

		self.pl = pl
		c = {}
		try:
			contexts, active_context = config.list_kube_config_contexts()
			c['context'] = active_context['name']
			c['namespace'] = active_context['context']['namespace']
		except Exception as e:
			if len(c) == 0:
				pl.error(e)
				return
			else:
				pass

		return self.build_segments(**c)


kubernetes = with_docstring(KubernetesSegment(),
		'''Return the current context.
		
		It will show the current context in config.
		It requires kubectl and kubernetes-py to be installed.
		
		Divider highlight group used: ``kubernetes:divider``.
		
		Highlight groups used: ``kubernetes``.
		''')

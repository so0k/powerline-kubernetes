# vim:fileencoding=utf-8:noet
from powerline.segments import Segment, with_docstring
from kubernetes import K8sConfig

class KubernetesSegment(Segment):

    def build_segments(self,context, namespace):
        segments = [
            {'contents': u'\U00002388 ', 'highlight_groups': ['kubernetes'], 'divider_highlight_group': 'kubernetes:divider'},
            {'contents': '%s - %s' % (context, namespace), 'highlight_groups': ['kubernetes'], 'divider_highlight_group': 'kubernetes:divider'},
        ]
	return segments

    def __call__(self, pl):
        pl.debug('Running powerline-kubernetes')

        self.pl = pl

	try:
            context = K8sConfig().current_context
	    namespace = K8sConfig().namespace
        except Exception as e:
            pl.error(e)
            return

        return self.build_segments(context,namespace)

kubernetes = with_docstring(KubernetesSegment(),
'''Return the current context.

It will show the current context in config.
It requires kubectl and kubernetes-py to be installed.

Divider highlight group used: ``kubernetes:divider``.

Highlight groups used: ``kubernetes``.
''')

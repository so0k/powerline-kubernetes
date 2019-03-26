from powerline.segments import Segment, with_docstring

import yaml
# This is to prevent a warning about unsafe loads because kubernetes_py uses yaml.load instead of yaml.safe_load
yaml.warnings({'YAMLLoadWarning': False})
try:
    from kubernetes_py import K8sConfig
except ImportError:
    # try the old name
    from kubernetes import K8sConfig

class KubernetesSegment(Segment):

    def build_segments(self, context, namespace):
        if namespace=='default':
            display_format = context
        else:
            display_format = '%s - %s' % (context, namespace)

        segments = [
            {'contents': u'\U00002388 ', 'highlight_groups': ['kubernetes'], 'divider_highlight_group': 'kubernetes:divider'},
            {'contents': display_format, 'highlight_groups': ['kubernetes'], 'divider_highlight_group': 'kubernetes:divider'},
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

# vim:fileencoding=utf-8:noet:tabstop=4:softtabstop=4:shiftwidth=4:expandtab:
import os
import yaml
from powerline.segments import Segment, with_docstring
from kubernetes.config import kube_config

class KubernetesSegment(Segment):
    _conf_yaml = None
    conf_yaml = os.path.expanduser(kube_config.KUBE_CONFIG_DEFAULT_LOCATION)


    def build_segments(self,context, namespace):
        segments = [
            {'contents': u'\U00002388 ', 'highlight_groups': ['kubernetes'], 'divider_highlight_group': 'kubernetes:divider'},
            {'contents': '%s - %s' % (context, namespace), 'highlight_groups': ['kubernetes'], 'divider_highlight_group': 'kubernetes:divider'},
        ]
        return segments

    @property
    def config(self):
        with open(self.conf_yaml, 'r') as f:
            if self._conf_yaml is None:
                self._conf_yaml = yaml.load(f)
        return self._conf_yaml

    def __call__(self, pl):
        pl.debug('Running powerline-kubernetes')
        self.pl = pl

        try:
            k8_loader = kube_config.KubeConfigLoader(self.config)
            current_context = k8_loader.current_context
            ctx = current_context['context']
            context = current_context['name']
            namespace = ctx['namespace']
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

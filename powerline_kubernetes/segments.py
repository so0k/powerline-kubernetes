# vim:fileencoding=utf-8:noet:tabstop=4:softtabstop=4:shiftwidth=4:expandtab:
import os
import yaml
from powerline.theme import requires_segment_info
from powerline.segments import Segment, with_docstring
from kubernetes.config import kube_config

_KUBERNETES = u'\U00002388 '

@requires_segment_info
class KubernetesSegment(Segment):
    conf_yaml = os.path.expanduser(kube_config.KUBE_CONFIG_DEFAULT_LOCATION)

    def kube_logo(self, color):
        return {
            'contents': _KUBERNETES,
            'highlight_groups': [color],
            'divider_highlight_group': 'kubernetes:divider'
        }

    def build_segments(self, context, namespace):
        alert = (context in self.alerts or namespace in self.alerts or context + ':' + namespace in self.alerts)
        segments = []

        if self.show_cluster:
            color = 'kubernetes_cluster:alert' if alert else 'kubernetes_cluster'
            if self.show_kube_logo:
                segments.append(self.kube_logo(color))

            segments.append({
                'contents': context,
                'highlight_groups': [color],
                'divider_highlight_group': 'kubernetes:divider'
            })

        if self.show_namespace:
            color = 'kubernetes_namespace:alert' if alert else 'kubernetes_namespace'

            if namespace != 'default' or self.show_default_namespace:
                if not self.show_cluster and self.show_kube_logo:
                    segments.append(self.kube_logo(color))

                segments.append({
                    'contents': namespace,
                    'highlight_groups': [color],
                    'divider_highlight_group': 'kubernetes:divider'
                })

        return segments

    @property
    def config(self):
        with open(self.conf_yaml, 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def __init__(self):
        self.pl = None
        self.show_kube_logo = None
        self.show_cluster = None
        self.show_namespace = None
        self.show_default_namespace = None
        self.kube_config_path = None
        self.alerts = []

    def __call__(
            self,
            pl,
            show_kube_logo=True,
            show_cluster=True,
            show_namespace=True,
            show_default_namespace=False,
            kube_config_path=None,
            alerts=[],
            **kwargs
        ):
        pl.debug('Running powerline-kubernetes')
        self.pl = pl
        self.show_kube_logo = show_kube_logo
        self.show_cluster = show_cluster
        self.show_namespace = show_namespace
        self.show_default_namespace = show_default_namespace
        self.kube_config_path = kube_config_path or self.conf_yaml
        self.alerts = alerts

        try:
            k8_loader = kube_config.KubeConfigLoader(self.config)
            current_context = k8_loader.current_context
            ctx = current_context['context']
            context = current_context['name']
        except Exception as e:
            pl.error(e)
            return
        try:
            namespace = ctx['namespace']
        except KeyError:
            namespace = 'default'


        return self.build_segments(context, namespace)

kubernetes = with_docstring(KubernetesSegment(),
'''Return the current context.

It will show the current context in config.
It requires kubectl and kubernetes-py to be installed.

Divider highlight group used: ``kubernetes:divider``.

Highlight groups used: ``kubernetes_cluster``,
``kubernetes_cluster:alert``, ``kubernetes_namespace``,
and ``kubernetes_namespace:alert``, .
''')

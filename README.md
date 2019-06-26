# Powerline Kubernetes [![PyPI version](https://badge.fury.io/py/powerline-kubernetes.svg)](https://badge.fury.io/py/powerline-kubernetes)

A [Powerline](https://github.com/powerline/powerline) segment to show the current Kubernetes context.

This segment shows the Kubernetes context together with a nice looking helm. Please feel free to propose more features and give me ideas on how to improve it.

<img src="screenshot.png" width="300">

## Requirements

The Kubernetes segment requires kubectl and official [kubernetes Python API](https://pypi.org/project/kubernetes/).

## Installation

Installing the Kubernetes segment can be done with `pip`:

```
$ pip install powerline-kubernetes
```

The Kubernetes segment uses a couple of custom highlight groups. You'll need to define those groups in your colorscheme, for example in `.config/powerline/colorschemes/default.json`:

```json
{
  "groups": {
    "kubernetes_cluster":         { "fg": "gray10", "bg": "darkestblue", "attrs": [] },
    "kubernetes_cluster:alert":   { "fg": "gray10", "bg": "darkestred",  "attrs": [] },
    "kubernetes_namespace":       { "fg": "gray10", "bg": "darkestblue", "attrs": [] },
    "kubernetes_namespace:alert": { "fg": "gray10", "bg": "darkred",     "attrs": [] },
    "kubernetes:divider":         { "fg": "gray4",  "bg": "darkestblue", "attrs": [] },
  }
}
```

Then you can activate the Kubernetes segment by adding it to your segment configuration, for example in `.config/powerline/themes/shell/default.json`:

```javascript
{
    "function": "powerline_kubernetes.kubernetes",
    "priority": 30,
    "args": {
        "show_kube_logo": true, // set to false to omit the Kube logo
        "show_cluster": true, // show cluster name
        "show_namespace": true, // show namespace name
        "show_default_namespace": false, // do not show namespace name if it's "default"
        "alerts": [
          "live", // show line in different color when namespace matches
          "cluster:live"  // show line in different color when cluster name and namespace match
        ]
    }
}
```

By default the segment will look for the Kubernetes config under `~/.kube/config`.


## License

Licensed under the [MIT License](LICENSE).

---

Inspired by [powerline-docker](https://github.com/adrianmo/powerline-docker).
Inspired by [powerkube](https://github.com/zcmarine/powerkube).
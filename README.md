# Powerline Kubernetes [![PyPI version](https://badge.fury.io/py/powerline-kubernetes.svg)](https://badge.fury.io/py/powerline-kubernetes)

A [Powerline](https://github.com/powerline/powerline) segment to show the current Kubernetes context.

This segment shows the Kubernetes context together with a nice looking helm. Please feel free to propose more features and give me ideas on how to improve it.

<img src="screenshot.png" width="300">

## Requirements

The Kubernetes segment requires kubectl and [kubernetes-py](https://pypi.python.org/pypi/kubernetes-py/).

## Installation

Installing the Kubernetes segment can be done with `pip`:

```
$ pip install powerline-kubernetes
```

The Kubernetes segment uses a couple of custom highlight groups. You'll need to define those groups in your colorscheme, for example in `.config/powerline/colorschemes/default.json`:

```json
{
  "groups": {
    "kubernetes":                { "fg": "gray8",           "bg": "darkestblue", "attrs": [] },
    "kubernetes:divider":        { "fg": "gray4",           "bg": "darkestblue", "attrs": [] },
    "kubernetes:alert":          { "fg": "gray8",           "bg": "darkred",     "attrs": [] }
  }
}
```

Then you can activate the Kubernetes segment by adding it to your segment configuration, for example in `.config/powerline/themes/shell/default.json`:

```json
{
    "function": "powerline_kubernetes.kubernetes",
    "priority": 30,
    "args": {
        "show_cluster": true, // show cluster name
        "show_namespace": true, // show namespace name
        "alert_namespaces": [
          "live", // show line in different color when namespace matches
          "cluster:live"  // show line in different color when cluster name and namespace matches
        ]
    }

}
```

By default the segment will look for the Kubernetes config under `~/.kube/config`.
## License

Licensed under the [MIT License](LICENSE).

---

Inspired by [powerline-docker](https://github.com/adrianmo/powerline-docker).

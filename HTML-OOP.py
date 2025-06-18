class HTMLElement:
    def __init__(self, tag, attrs=None, children=None, self_closing=False):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = children or []
        self.self_closing = self_closing

    def render_attrs(self):
        return ' '.join(f'{k}="{v}"' for k, v in self.attrs.items())

    def render(self):
        attrs_str = self.render_attrs()
        if self.self_closing:
            return f'<{self.tag} {attrs_str} />'.strip()
        children_str = ''.join(child.render() if isinstance(child, HTMLElement) else str(child) for child in self.children)
        return f'<{self.tag} {attrs_str}>{children_str}</{self.tag}>'.strip()


class Input(HTMLElement):
    def __init__(self, type_, name, value=''):
        super().__init__('input', {'type': type_, 'name': name, 'value': value}, self_closing=True)


class Select(HTMLElement):
    def __init__(self, name, options):
        children = [HTMLElement('option', {'value': val}, [label]) for val, label in options]
        super().__init__('select', {'name': name}, children)


class Anchor(HTMLElement):
    def __init__(self, href, text):
        super().__init__('a', {'href': href}, [text])


class Image(HTMLElement):
    def __init__(self, src, alt=''):
        super().__init__('img', {'src': src, 'alt': alt}, self_closing=True)


class Div(HTMLElement):
    def __init__(self, children=None, attrs=None):
        super().__init__('div', attrs, children)


class Form(HTMLElement):
    def __init__(self, action, method, children=None):
        super().__init__('form', {'action': action, 'method': method}, children)



form = Form(
    action="/submit",
    method="post",
    children=[
        Div(children=[
            Input("text", "username"),
            Input("password", "password"),
        ]),
        Div(children=[
            Select("gender", [("m", "Male"), ("f", "Female")]),
        ]),
        Div(children=[
            Anchor("/help", "Need help?"),
        ]),
        Div(children=[
            Image("/logo.png", "Logo"),
        ]),
        Div(children=[
            Input("submit", "submit", "Send"),
        ])
    ]
)

print(form)
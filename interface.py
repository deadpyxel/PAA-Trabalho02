from gi.repository import Gtk  # importa recusrsos para interface gráfica

from huffman import huffman_encode  # importa a função de enconding para codificação de huffman
from lcs import lcs  # importa a função principal da lcs


# TODO integrar chain Matrix Multiplication com a UI

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PAA - Trabalho 02")
        self.set_border_width(10)
        self.set_default_size(500, 400)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Assignment Problem
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        label = Gtk.Label("Aqui tera o conteudo do primeiro exercicio do trabalho...")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        self.page1.add(label)
        self.notebook.append_page(self.page1, Gtk.Label("Associação de Tarefas"))

        # Huffman Coding
        self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.page2.set_border_width(10)
        label = Gtk.Label()
        label.set_markup("<big><b>Codificação de Huffman</b></big>")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        # Form
        self.lbl_inp_text = Gtk.Label("Digite o texto para codificação e compressão: ")
        self.txt_inp_text = Gtk.Entry()
        self.hbox_btn = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.btn_lcs = Gtk.Button(label="Codificar e Comprimir")
        self.btn_lcs.connect("clicked", self.huffman_call)  # executa a codificação
        self.btn_clear = Gtk.Button(label="Limpar Campo")
        self.btn_clear.connect("clicked", self.clear)  # limpa os campos
        self.hbox_btn.pack_start(self.btn_lcs, True, True, 0)
        self.hbox_btn.add(self.btn_clear)
        self.page2.add(label)
        self.page2.pack_start(self.lbl_inp_text, True, True, 0)
        self.page2.pack_start(self.txt_inp_text, True, True, 0)
        self.page2.pack_start(self.hbox_btn, True, True, 0)
        self.notebook.append_page(self.page2, Gtk.Label("Codificação de Huffman"))

        # Fractional Knapsack
        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        label = Gtk.Label("Aqui tera o conteudo do terceiro exercicio do trabalho...")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        self.page3.add(label)
        self.notebook.append_page(self.page3, Gtk.Label("Mochila Fracionária"))

        # 0-1 Knapsack
        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        label = Gtk.Label("Aqui tera o conteudo do quarto exercicio do trabalho...")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        self.page4.add(label)
        self.notebook.append_page(self.page4, Gtk.Label("Mochila Booleana"))

        # Longest Common Substring
        self.page5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.page5.set_border_width(10)
        # Label do exercicio
        label = Gtk.Label()
        label.set_markup("<big><b>Longest Common Substring</b></big>")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        # Form
        self.lbl_grpa = Gtk.Label("Substring para verificação: ")
        self.txt_grpa = Gtk.Entry()
        self.lbl_grpb = Gtk.Label("String para a busca: ")
        self.txt_grpb = Gtk.Entry()
        self.hbox_btn = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.btn_lcs = Gtk.Button(label="Verificar Substrings")
        self.btn_lcs.connect("clicked", self.lcs_call)  # executa o lcs
        self.btn_clear = Gtk.Button(label="Limpar Campos")
        self.btn_clear.connect("clicked", self.clear)  # limpa os campos
        self.hbox_btn.pack_start(self.btn_lcs, True, True, 0)
        self.hbox_btn.add(self.btn_clear)
        self.page5.add(label)
        self.page5.pack_start(self.lbl_grpa, True, True, 0)
        self.page5.pack_start(self.txt_grpa, True, True, 0)
        self.page5.pack_start(self.lbl_grpb, True, True, 0)
        self.page5.pack_start(self.txt_grpb, True, True, 0)
        self.page5.add(self.hbox_btn)
        self.notebook.append_page(self.page5, Gtk.Label("LCS"))

        # Chain Matrix Multiplication
        self.page6 = Gtk.Box()
        self.page6.set_border_width(10)
        label = Gtk.Label("Aqui tera o conteudo do sexto exercicio do trabalho...")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        self.page6.add(label)
        self.notebook.append_page(self.page6, Gtk.Label("Multiplicação de Cadeia de Matrizes"))

    def huffman_call(self, widget):
        inp_str = self.txt_inp_text.get_text()
        out_code, out_encoded = huffman_encode(inp_str)
        # print(out_code, out_encoded)
        print("Tamanho original da string: ", len(inp_str))
        print("Tamanho após codificação: ", len(out_encoded))

    def lcs_call(self, widget):
        str_a = self.txt_grpa.get_text()
        str_b = self.txt_grpb.get_text()
        str_result = lcs(str_a, str_b)
        dialog = DialogWindow(self, str_result)
        dialog.run()
        dialog.destroy()

    def clear(self, widget):
        self.txt_inp_text.set_text("")
        self.txt_grpa.set_text("")
        self.txt_grpb.set_text("")


class DialogWindow(Gtk.Dialog):
    def __init__(self, parent, str_result):
        Gtk.Dialog.__init__(self, "Resultados do LCS", parent, Gtk.DialogFlags.MODAL, (
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))
        self.set_default_size(200, 100)
        self.set_border_width(10)

        area = self.get_content_area()
        area.add(Gtk.Label("A maior substring encontrada foi: \n"))
        lbl_result = Gtk.Label()
        lbl_result.set_markup("<big><b>" + str_result + "</b></big>")
        area.add(lbl_result)
        self.show_all()


def main():
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()

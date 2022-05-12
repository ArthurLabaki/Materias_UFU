#include <gtk/gtk.h>
#include <gdk/gdkkeysyms.h>
#include <cairo.h>
#include <stdlib.h>

// Comando para compilar a main.c
// gcc -o main main.c `pkg-config --libs --cflags gtk+-2.0`

// Função do contador de cliques

static int contador = 0;

void contadorCliques(GtkWidget *widget, gpointer nomeWidget);

void abrirEditorTexto(GtkWidget *widget, gpointer nomeWidget);

void abrirExploradorArquivos(GtkWidget *widget, gpointer nomeWidget);

void abrirNavegador(GtkWidget *widget, gpointer nomeWidget);

gboolean on_expose_event(GtkWidget *widget, GdkEventExpose *event, gpointer nomeWidget);

gboolean time_handler(GtkWidget *widget);

int mostrarPopup(GtkWidget *widget, GdkEvent *event);

int main(int argc, char *argv[]){

    GtkWidget *janela, *botao, *fixed, *toolbar, *relogio;
    GtkToolItem *fechar, *separador, *editorTexto, *exploradorArquivos, *web;
    GtkWidget *label, *toolbar2, *barraSuperior1, *barraSuperior2;
    GtkWidget *menuPopup, *minimizar, *encerrar;
    
    //GtkWidget *pmenu, *hideMi, *menubar, *fileMenu, *fileMi;
    //GtkWidget *newMi, *openMi, *quitMi, *toolbar, *newTb;
    //GtkWidget *openTb, *saveTb, *sep, *exitTb;

    GdkColor cor;

    GtkAccelGroup *accel_group = NULL;

    // Início da manipulação dos widgets

    gtk_init (&argc, &argv);

    // Criar a tela do shell gráfico

    janela = gtk_window_new(GTK_WINDOW_TOPLEVEL); // Criar uma nova janela
    gtk_window_set_title(GTK_WINDOW(janela), "Shell Grafico GBC046"); // Título da janela do shell
    gtk_window_fullscreen(GTK_WINDOW(janela)); // Criar tela em fullsreen

    // Criar botão "Clique aqui!"

    fixed = gtk_fixed_new(); // Widget que coloca os filhos em posições e define tamanhos fixos
    gtk_container_add(GTK_CONTAINER(janela), fixed);

    botao = gtk_button_new_with_label("Clique aqui!");
    
    g_signal_connect(GTK_OBJECT(botao), "clicked", G_CALLBACK(contadorCliques), "Botao");

    // Obs: A minha tela possui resolução de 1366 x 768

	gtk_fixed_put(GTK_FIXED(fixed), botao, 583, 334); // Posição na tela (descontar 50 px do botão)
	gtk_widget_set_size_request(botao, 200, 100); // Tamanho do botão

    // Criar a toolbar

    toolbar = gtk_toolbar_new();
    gtk_toolbar_set_style(GTK_TOOLBAR(toolbar), GTK_TOOLBAR_ICONS);

    fechar = gtk_tool_button_new_from_stock(GTK_STOCK_CLOSE);
    gtk_toolbar_insert(GTK_TOOLBAR(toolbar), fechar, -1); // Inserir o botão de fechar a janela

    separador = gtk_separator_tool_item_new();
    gtk_toolbar_insert(GTK_TOOLBAR(toolbar), separador, -1); // Inserir a barra de separação de ícones

    editorTexto = gtk_tool_button_new_from_stock(GTK_STOCK_NEW);
    gtk_toolbar_insert(GTK_TOOLBAR(toolbar), editorTexto, -1); // Inserir o botão de abrir novo arquivo de texto

    exploradorArquivos = gtk_tool_button_new_from_stock(GTK_STOCK_DIRECTORY);
    gtk_toolbar_insert(GTK_TOOLBAR(toolbar), exploradorArquivos, -1); // Inserir o botão do explorador de arquivos

    web = gtk_tool_button_new_from_stock(GTK_STOCK_INFO);
    gtk_toolbar_insert(GTK_TOOLBAR(toolbar), web, -1); // Inserir o botão de abrir novo arquivo de texto

    // Modificação da cor da toolbar

    gdk_color_parse("#777777", &cor); // Código da cor em hexadecimal
  	gtk_widget_modify_bg(toolbar, GTK_STATE_NORMAL, &cor); // Modificar a cor de fundo do widget

    // Ações para cada botão criado acima

    // gtk_fixed_put(GTK_FIXED(fixed), toolbar, 0, 979); // Configuração para a tela do Paulo
	
    gtk_fixed_put(GTK_FIXED(fixed), toolbar, 0, 723); // Configuração para a tela do Pedro
	gtk_widget_set_size_request(toolbar, 1366, 45);

	g_signal_connect(G_OBJECT(fechar), "clicked", G_CALLBACK(gtk_main_quit), NULL);

	g_signal_connect(G_OBJECT(editorTexto), "clicked", G_CALLBACK(abrirEditorTexto), NULL);
	
	g_signal_connect(G_OBJECT(exploradorArquivos), "clicked", G_CALLBACK(abrirExploradorArquivos), NULL);

    g_signal_connect(G_OBJECT(web), "clicked", G_CALLBACK(abrirNavegador), NULL);

	g_signal_connect(G_OBJECT(janela), "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Criar o relógio

    relogio = gtk_drawing_area_new();

    //gtk_fixed_put(GTK_FIXED(fixed), relogio, 1175, 980); // Configuração para a tela do Paulo
	
    gtk_fixed_put(GTK_FIXED(fixed), relogio, 1255, 723);
  	gtk_widget_set_size_request(relogio, 100, 30);

    gdk_color_parse("#777777", &cor); // Mudar a cor de fundo do relógio
  	gtk_widget_modify_bg(relogio, GTK_STATE_NORMAL, &cor);

    g_signal_connect(relogio, "expose-event", G_CALLBACK(on_expose_event), NULL); // Identifica que a tela foi aberta

    g_timeout_add(1000, (GSourceFunc) time_handler, (gpointer) janela);
	time_handler(relogio);

    // Criar uma label em cima de uma toolbar (2)

    toolbar2 = gtk_toolbar_new();

    gdk_color_parse("#777777", &cor); // Código da cor em hexadecimal
  	gtk_widget_modify_bg(toolbar2, GTK_STATE_NORMAL, &cor); // Modificar a cor de fundo do widget

    gtk_fixed_put(GTK_FIXED(fixed), toolbar2, 508, 0); // Configuração para a tela do Pedro
	gtk_widget_set_size_request(toolbar2, 350, 45);

    label = gtk_label_new(NULL);

    gtk_fixed_put(GTK_FIXED(fixed), label, 508, 0); // Configuração para a tela do Pedro
	gtk_widget_set_size_request(label, 350, 45);
    gtk_label_set_markup(GTK_LABEL(label), "<span font = \"12\" color = \"white\"> Shell Grafico - Sistemas Operacionais (GBC045) </span>");

    // Criar barra superior 1

    barraSuperior1 = gtk_event_box_new();
  	gtk_fixed_put(GTK_FIXED(fixed), barraSuperior1, 0, 0);
	gtk_widget_set_size_request(barraSuperior1, 508, 45);

  	menuPopup = gtk_menu_new();
  
	minimizar = gtk_menu_item_new_with_label("Minimizar");
	gtk_widget_show(minimizar);
	gtk_menu_shell_append(GTK_MENU_SHELL(menuPopup), minimizar);

	encerrar = gtk_menu_item_new_with_label("Encerrar shell");
    gtk_widget_show(encerrar);
	gtk_menu_shell_append(GTK_MENU_SHELL(menuPopup), encerrar);

	g_signal_connect_swapped(G_OBJECT(minimizar), "activate", G_CALLBACK(gtk_window_iconify), GTK_WINDOW(janela));    

	g_signal_connect(G_OBJECT(encerrar), "activate", G_CALLBACK(gtk_main_quit), NULL);

	g_signal_connect(G_OBJECT(janela), "destroy", G_CALLBACK(gtk_main_quit), NULL);
	    
	g_signal_connect_swapped(G_OBJECT(barraSuperior1), "button-press-event", G_CALLBACK(mostrarPopup), menuPopup);

	gdk_color_parse("#777777", &cor); // Modificar a cor da barra superior 1
  	gtk_widget_modify_bg(barraSuperior1, GTK_STATE_NORMAL, &cor); //modifying the background color of the widget

    // Criar barra superior 2
    
    barraSuperior2 = gtk_event_box_new();
  	gtk_fixed_put(GTK_FIXED(fixed), barraSuperior2, 858, 0);
	gtk_widget_set_size_request(barraSuperior2, 508, 45);

	g_signal_connect_swapped(G_OBJECT(minimizar), "activate", G_CALLBACK(gtk_window_iconify), GTK_WINDOW(janela));    

	g_signal_connect(G_OBJECT(encerrar), "activate", G_CALLBACK(gtk_main_quit), NULL);

	g_signal_connect(G_OBJECT(janela), "destroy", G_CALLBACK(gtk_main_quit), NULL);
	    
	g_signal_connect_swapped(G_OBJECT(barraSuperior2), "button-press-event", G_CALLBACK(mostrarPopup), menuPopup);

	gdk_color_parse("#777777", &cor); // Modificar a cor da barra superior 1
  	gtk_widget_modify_bg(barraSuperior2, GTK_STATE_NORMAL, &cor); //modifying the background color of the widget
    
    // Fim da manipulação dos widgets

    gtk_widget_show_all(janela); // Exibir a tela criada
    gtk_main(); // Fim

    return 0;

}

void contadorCliques(GtkWidget *widget, gpointer nomeWidget){

    g_print("\n%s foi clicado %d vez(es)\n", (char*)nomeWidget, ++contador);

}

void abrirEditorTexto(GtkWidget *widget, gpointer nomeWidget){

    system("gedit");

    // Aqui pode-se criar um thread para executar o gedit

}

void abrirExploradorArquivos(GtkWidget *widget, gpointer nomeWidget){

    system("nautilus"); // Nautilus é o file explorer do Ubuntu

    // Aqui pode-se criar um thread para executar o explorador de arquivos

}

void abrirNavegador(GtkWidget *widget, gpointer nomeWidget){

    system("firefox"); // Nautilus é o file explorer do Ubuntu

    // Aqui pode-se criar um thread para executar o navegador
}

void destroy(GtkWidget* widget, gpointer nomeWidget){
    
	gtk_main_quit();

}

gchar buf[256];

gboolean on_expose_event(GtkWidget *widget, GdkEventExpose *event, gpointer nomeWidget){
        
    cairo_t *cr;

    cr = gdk_cairo_create(widget->window);

    cairo_move_to(cr, 30, 30);
    cairo_set_font_size(cr, 15);
    cairo_show_text(cr, buf);

    cairo_destroy(cr);

    return FALSE;

}

gboolean time_handler(GtkWidget *widget){
    
    if(widget->window == NULL){
        return FALSE;
    }

    GDateTime *now = g_date_time_new_now_local(); 
    gchar *my_time = g_date_time_format(now, "%H:%M:%S");
    
    g_sprintf(buf, "%s", my_time);
    
    g_free(my_time);
    g_date_time_unref(now);

    gtk_widget_queue_draw(widget);
    
    return TRUE;

}

int mostrarPopup(GtkWidget *widget, GdkEvent *event) {
  
  const gint RIGHT_CLICK = 3;
    
  if (event->type == GDK_BUTTON_PRESS) {
      
      GdkEventButton *bevent = (GdkEventButton *) event;
      
      if (bevent->button == RIGHT_CLICK) {      
          
          gtk_menu_popup(GTK_MENU(widget), NULL, NULL, NULL, NULL,
              bevent->button, bevent->time);
          }
          
      return TRUE;
  }

  return FALSE;
}
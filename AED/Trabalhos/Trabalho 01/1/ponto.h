typedef struct coordenadas *ponto;
ponto criaPonto(ponto A, int x, int y);
float calculaDistancia(ponto A, ponto B);
int getValorX(ponto A);
int getValorY(ponto A);
void liberarPonto(ponto A);

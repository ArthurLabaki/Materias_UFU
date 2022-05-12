package teste;

public class Factory2D extends AbstractFactory{ // Concrete factory 2D

    public Copo fabricarCopo() {
        return new Copo2D();
    }

    public Garrafa fabricarGarrafa() {
        return new Garrafa2D();
    }

    public Prato fabricarPrato() {
        return new Prato2D();
    }
    
}

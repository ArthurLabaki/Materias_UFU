package teste;

public class Factory3D extends AbstractFactory{ // Concrete factory 3D

    public Copo fabricarCopo() {
        return new Copo3D();
    }

    public Garrafa fabricarGarrafa() {
        return new Garrafa3D();
    }

    public Prato fabricarPrato() {
        return new Prato3D();
    }
    
}
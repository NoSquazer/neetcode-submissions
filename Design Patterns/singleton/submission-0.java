static class Singleton {
    public static Singleton uniqueInstance = null;
    private String value = null;

    private Singleton() {
        this.value = null;
    }

    public static Singleton getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}

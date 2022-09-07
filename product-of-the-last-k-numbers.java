class ProductOfNumbers {
    private List<Integer> products;
    
    public ProductOfNumbers() {
        products = new ArrayList();
        products.add(1);
    }

    public void add(int num) {
        if (num == 0) {
            products = new ArrayList();
            products.add(1);
        } else {
            products.add(num * products.get(products.size() - 1));
        }
        
    }

    public int getProduct(int k) {
        if (k > products.size() - 1) {
            return 0;
        } else {
            return products.get(products.size() - 1) / products.get(products.size() - k - 1);
        }
    }
}

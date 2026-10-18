export class Cart {
  constructor(items = []) {
    this.items = items;
  }

  add(item) {
    const existing = this.items.find((entry) => entry.sku === item.sku);
    if (existing) {
      existing.quantity += item.quantity;
      return existing;
    }
    this.items.push({ ...item });
    return item;
  }

  remove(sku) {
    this.items = this.items.filter((entry) => entry.sku !== sku);
  }

  get totalCents() {
    return this.items.reduce(
      (sum, entry) => sum + entry.priceCents * entry.quantity,
      0,
    );
  }

  get isEmpty() {
    return this.items.length === 0;
  }
}

import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { ItemDefinition, ItemDefinition2 } from '../../services/models';
import { BasketService } from '../../services/basket.service';

@Component({
  selector: 'app-item-details',
  templateUrl: './item-details.component.html',
  styleUrl: './item-details.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ItemDetailsComponent {
  @Input() itemDef?: ItemDefinition2;

  constructor(private basketService: BasketService) {}

  addToBusket(): void {
    this.basketService.addItemToBasket({
      productId: this.itemDef!.product_id,
      quantity: 1,
    });
  }
}

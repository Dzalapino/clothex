import { Component, OnInit } from '@angular/core';
import { ItemService } from '../../services/items.service';
import { ActivatedRoute, Params } from '@angular/router';
import { switchMap } from 'rxjs';
import { ItemDefinition } from '../../services/models';
import { error } from 'console';
import { ToastrService } from 'ngx-toastr';
import { BasketService } from '../../services/basket.service';

@Component({
  selector: 'app-item-details-page',
  templateUrl: './item-details-page.component.html',
  styleUrl: './item-details-page.component.scss',
})
export class ItemDetailsPageComponent implements OnInit {
  item?: ItemDefinition;

  constructor(
    private itemService: ItemService,
    private route: ActivatedRoute,
    private toastrService: ToastrService,
    private basketService: BasketService
  ) {}

  addToBusket(): void {
    this.basketService.addItemToBasket({
      productId: this.item!.id,
      quantity: 1,
    });
  }

  ngOnInit(): void {
    this.route.params
      .pipe(
        switchMap((params: Params) =>
          this.itemService.getItemById(+params['id'])
        )
      )
      .subscribe(
        (res) => {
          this.item = res;
        },
        (error) => {
          this.toastrService.error(error.error.detail);
        }
      );
  }
}

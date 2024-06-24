import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
} from '@angular/core';
import { ItemService } from '../../services/items.service';
import { ItemDefinition2, ItemStock } from '../../services/models';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent implements OnInit {
  itemStock: ItemStock[] = [];

  itemDefinitions: Array<ItemDefinition2[]> = [];

  constructor(
    public itemService: ItemService,
    private toastr: ToastrService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.itemService.getItemsStock().subscribe((stock) => {
      this.itemStock = stock;
      this.cdr.markForCheck();
    });

    this.itemService.getData().subscribe((res) => {
      this.itemDefinitions = res;
      this.cdr.markForCheck();
    });
  }
}

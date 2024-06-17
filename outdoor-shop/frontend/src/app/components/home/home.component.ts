import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { ItemService } from '../../services/items.service';
import { ItemDefinition, ItemStock } from '../../services/models';
import { ToastrService } from 'ngx-toastr';
import { error } from 'console';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent implements OnInit {
  itemDefs: ItemDefinition[] = [];
  itemStock: ItemStock[] = [];

  constructor(public itemService: ItemService, private toastr: ToastrService) {}

  ngOnInit(): void {
    this.itemService.getItemDefinitions().subscribe(
      (defs) => {
        this.itemDefs = defs;
      },
      (error) => {
        this.toastr.error('Could not fetch item definitions!');
      }
    );
    this.itemService.getItemsStock().subscribe(
      (stock) => {
        this.itemStock = stock;
      },
      (error) => {
        this.toastr.error('Could not stocks!');
      }
    );
  }

  getItemDefById(id: string): ItemDefinition | undefined {
    return this.itemDefs.filter((item) => item.id === id).at(0);
  }
}

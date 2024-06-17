import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { ItemDefinition } from '../../services/models';

@Component({
  selector: 'app-item-details',
  templateUrl: './item-details.component.html',
  styleUrl: './item-details.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ItemDetailsComponent {
  @Input() itemDef?: ItemDefinition;
  @Input() quantity?: number;

  buyItem(): void {
    console.log(this.itemDef?.id);
  }
}

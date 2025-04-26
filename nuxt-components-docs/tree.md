<!-- source: https://ui.nuxt.com/components/tree --> # Tree

[Tree](https://reka-
ui.com/docs/components/tree)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Tree.vue)

A tree view component to display and interact with hierarchical data
structures.

## Usage

### Items

Use the `items` prop as an array of objects with the following properties:

  * `icon?: string`
  * `label?: string`
  * `trailingIcon?: string`
  * `defaultExpanded?: boolean`
  * `disabled?: boolean`
  * `value?: string`
  * `slot?: string`
  * `children?: TreeItem[]`
  * `onToggle?(e: Event): void`
  * `onSelect?(e?: Event): void`

A unique identifier is required for each item. The component will use the
`value` prop as identifier, falling back to `label` if `value` is not
provided. One of these must be provided for the component to work properly.

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              {
                label: 'Card.vue',
                icon: 'i-vscode-icons-file-type-vue'
              },
              {
                label: 'Button.vue',
                icon: 'i-vscode-icons-file-type-vue'
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree :items="items" />
    </template>
    

Expand code

### Multiple

Use the `multiple` prop to allow multiple item selections.

multiple

true

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              {
                label: 'Card.vue',
                icon: 'i-vscode-icons-file-type-vue'
              },
              {
                label: 'Button.vue',
                icon: 'i-vscode-icons-file-type-vue'
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree multiple :items="items" />
    </template>
    

Expand code

### Color

Use the `color` prop to change the color of the Tree.

color

neutral

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              {
                label: 'Card.vue',
                icon: 'i-vscode-icons-file-type-vue'
              },
              {
                label: 'Button.vue',
                icon: 'i-vscode-icons-file-type-vue'
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree color="neutral" :items="items" />
    </template>
    

Expand code

### Size

Use the `size` prop to change the size of the Tree.

size

xl

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              {
                label: 'Card.vue',
                icon: 'i-vscode-icons-file-type-vue'
              },
              {
                label: 'Button.vue',
                icon: 'i-vscode-icons-file-type-vue'
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree size="xl" :items="items" />
    </template>
    

Expand code

### Trailing Icon

Use the `trailing-icon` prop to customize the trailing
[Icon](/components/icon) of a parent node. Defaults to `i-lucide-chevron-
down`.

If an icon is specified for an item, it will always take precedence over these
props.

trailingIcon

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            trailingIcon: 'i-lucide-chevron-down',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              {
                label: 'Card.vue',
                icon: 'i-vscode-icons-file-type-vue'
              },
              {
                label: 'Button.vue',
                icon: 'i-vscode-icons-file-type-vue'
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree trailing-icon="i-lucide-arrow-down" :items="items" />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.chevronDown` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.chevronDown` key.

### Expanded Icon

Use the `expanded-icon` and `collapsed-icon` props to customize the icons of a
parent node when it is expanded or collapsed. Defaults to `i-lucide-folder-
open` and `i-lucide-folder` respectively.

expandedIcon

collapsedIcon

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              {
                label: 'Card.vue',
                icon: 'i-vscode-icons-file-type-vue'
              },
              {
                label: 'Button.vue',
                icon: 'i-vscode-icons-file-type-vue'
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree expanded-icon="i-lucide-book-open" collapsed-icon="i-lucide-book" :items="items" />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize these icons globally in
your `app.config.ts` under `ui.icons.folder` and `ui.icons.folderOpen` keys.

[](/getting-started/icons/vue#theme)You can customize these icons globally in
your `vite.config.ts` under `ui.icons.folder` and `ui.icons.folderOpen` keys.

### Disabled

Use the `disabled` prop to prevent any user interaction with the Tree.

You can also disable individual items using `item.disabled`.

disabled

true

  * app
    * composables
    * components
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'app',
        icon: 'i-lucide-folder',
        defaultExpanded: true,
        children: [
          {
            label: 'composables',
            icon: 'i-lucide-folder',
            children: [
              {
                label: 'useAuth.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              },
              {
                label: 'useUser.ts',
                icon: 'i-vscode-icons-file-type-typescript'
              }
            ]
          },
          {
            label: 'components',
            icon: 'i-lucide-folder',
            children: [
              {
                label: 'Home',
                icon: 'i-lucide-folder',
                children: [
                  {
                    label: 'Card.vue',
                    icon: 'i-vscode-icons-file-type-vue'
                  },
                  {
                    label: 'Button.vue',
                    icon: 'i-vscode-icons-file-type-vue'
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        label: 'app.vue',
        icon: 'i-vscode-icons-file-type-vue'
      },
      {
        label: 'nuxt.config.ts',
        icon: 'i-vscode-icons-file-type-nuxt'
      }
    ])
    </script>
    
    <template>
      <UTree disabled :items="items" />
    </template>
    

Expand code

## Examples

### Control selected item(s)

You can control the selected item(s) by using the `default-value` prop or the
`v-model` directive.

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    import type { TreeItem } from '@nuxt/ui'
    
    const items: TreeItem[] = [
      {
        label: 'app/',
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              { label: 'useAuth.ts', icon: 'i-vscode-icons-file-type-typescript' },
              { label: 'useUser.ts', icon: 'i-vscode-icons-file-type-typescript' }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              { label: 'Card.vue', icon: 'i-vscode-icons-file-type-vue' },
              { label: 'Button.vue', icon: 'i-vscode-icons-file-type-vue' }
            ]
          }
        ]
      },
      { label: 'app.vue', icon: 'i-vscode-icons-file-type-vue' },
      { label: 'nuxt.config.ts', icon: 'i-vscode-icons-file-type-nuxt' }
    ]
    
    const value = ref()
    </script>
    
    <template>
      <UTree v-model="value" :items="items" />
    </template>
    

Expand code

If you want to prevent an item from being selected, you can use the
`item.onSelect()` property:

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    import type { TreeItem } from '@nuxt/ui'
    
    const items: TreeItem[] = [
      {
        label: 'app/',
        defaultExpanded: true,
        onSelect: (e: Event) => {
          e.preventDefault()
        },
        children: [
          {
            label: 'composables/',
            children: [
              { label: 'useAuth.ts', icon: 'i-vscode-icons-file-type-typescript' },
              { label: 'useUser.ts', icon: 'i-vscode-icons-file-type-typescript' }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              { label: 'Card.vue', icon: 'i-vscode-icons-file-type-vue' },
              { label: 'Button.vue', icon: 'i-vscode-icons-file-type-vue' }
            ]
          }
        ]
      },
      { label: 'app.vue', icon: 'i-vscode-icons-file-type-vue' },
      { label: 'nuxt.config.ts', icon: 'i-vscode-icons-file-type-nuxt' }
    ]
    </script>
    
    <template>
      <UTree :items="items" />
    </template>
    

Expand code

This lets you expand or collapse a parent item without selecting it.

### Control expanded items

You can control the expanded items by using the `default-expanded` prop or the
`v-model` directive.

  * app/
    * composables/
      * useAuth.ts
      * useUser.ts
    * components/
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    import type { TreeItem } from '@nuxt/ui'
    
    const items: TreeItem[] = [
      {
        label: 'app/',
        value: 'app',
        children: [
          {
            label: 'composables/',
            value: 'composables',
            children: [
              { label: 'useAuth.ts', icon: 'i-vscode-icons-file-type-typescript' },
              { label: 'useUser.ts', icon: 'i-vscode-icons-file-type-typescript' }
            ]
          },
          {
            label: 'components/',
            value: 'components',
            children: [
              { label: 'Card.vue', icon: 'i-vscode-icons-file-type-vue' },
              { label: 'Button.vue', icon: 'i-vscode-icons-file-type-vue' }
            ]
          }
        ]
      },
      { label: 'app.vue', icon: 'i-vscode-icons-file-type-vue' },
      { label: 'nuxt.config.ts', icon: 'i-vscode-icons-file-type-nuxt' }
    ]
    
    const expanded = ref(['app', 'composables'])
    </script>
    
    <template>
      <UTree v-model:expanded="expanded" :items="items" />
    </template>
    

Expand code

If you want to prevent an item from being expanded, you can use the
`item.onToggle()` property:

  * app/
    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    import type { TreeItem } from '@nuxt/ui'
    
    const items: TreeItem[] = [
      {
        label: 'app/',
        defaultExpanded: true,
        onToggle: (e: Event) => {
          e.preventDefault()
        },
        children: [
          {
            label: 'composables/',
            children: [
              { label: 'useAuth.ts', icon: 'i-vscode-icons-file-type-typescript' },
              { label: 'useUser.ts', icon: 'i-vscode-icons-file-type-typescript' }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              { label: 'Card.vue', icon: 'i-vscode-icons-file-type-vue' },
              { label: 'Button.vue', icon: 'i-vscode-icons-file-type-vue' }
            ]
          }
        ]
      },
      { label: 'app.vue', icon: 'i-vscode-icons-file-type-vue' },
      { label: 'nuxt.config.ts', icon: 'i-vscode-icons-file-type-nuxt' }
    ]
    </script>
    
    <template>
      <UTree :items="items" />
    </template>
    

Expand code

This lets you select a parent item without expanding or collapsing its
children.

### With custom slot

Use the `item.slot` property to customize a specific item.

  * app/

    * composables/
    * components/
      * Card.vue
      * Button.vue
  * app.vue
  * nuxt.config.ts

    
    
    <script setup lang="ts">
    import type { TreeItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'app/',
        slot: 'app' as const,
        defaultExpanded: true,
        children: [
          {
            label: 'composables/',
            children: [
              { label: 'useAuth.ts', icon: 'i-vscode-icons-file-type-typescript' },
              { label: 'useUser.ts', icon: 'i-vscode-icons-file-type-typescript' }
            ]
          },
          {
            label: 'components/',
            defaultExpanded: true,
            children: [
              { label: 'Card.vue', icon: 'i-vscode-icons-file-type-vue' },
              { label: 'Button.vue', icon: 'i-vscode-icons-file-type-vue' }
            ]
          }
        ]
      },
      { label: 'app.vue', icon: 'i-vscode-icons-file-type-vue' },
      { label: 'nuxt.config.ts', icon: 'i-vscode-icons-file-type-nuxt' }
    ] satisfies TreeItem[]
    </script>
    
    <template>
      <UTree :items="items">
        <template #app="{ item }">
          <p class="italic font-bold">
            {{ item.label }}
          </p>
        </template>
      </UTree>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'ul'`| `any`The element or component this component should render as.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`valueKey`| `'value'`| ` string | number`The key used to get the value from the item.  
`labelKey`| `'label'`| ` string | number`The key used to get the label from the item.  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
on the right side of a parent node.  
`expandedIcon`| `appConfig.ui.icons.folderOpen`| ` string`The icon displayed
when a parent node is expanded.  
`collapsedIcon`| `appConfig.ui.icons.folder`| ` string`The icon displayed when
a parent node is collapsed.  
`items`| | ` TreeItem[]`Show properties

  * `icon?: string`
  * `label?: string`
  * `trailingIcon?: string`
  * `defaultExpanded?: boolean`
  * `disabled?: boolean`
  * `value?: string`
  * `slot?: string`
  * `children?: TreeItem[]`
  * `onToggle?: ((e: Event) => void)`
  * `onSelect?: ((e?: Event ) => void) | undefined`

  
`modelValue`| | `any`The controlled value of the Tree. Can be bind as `v-model`.  
`defaultValue`| | `any`The value of the Tree when initially rendered. Use when you do not need to control the state of the Tree.  
`multiple`| | `boolean`Whether multiple options can be selected or not.  
`defaultExpanded`| | ` string[]`The value of the expanded tree when initially rendered. Use when you do not need to control the state of the expanded tree  
`disabled`| | `boolean`When `true`, prevents the user from interacting with tree  
`expanded`| | ` string[]`The controlled value of the expanded item. Can be binded with with `v-model`.  
`selectionBehavior`| | ` "toggle" | "replace"`How multiple selection should behave in the collection.  
`propagateSelect`| | `boolean`When `true`, selecting parent will select the descendants.  
`ui`| | ` { root?: ClassNameValue; item?: ClassNameValue; listWithChildren?: ClassNameValue; itemWithChildren?: ClassNameValue; ... 4 more ...; linkTrailingIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`item`| `{ item: TreeItem; index: number; level: number; expanded: boolean;
selected: boolean; }`  
`item-leading`| `{ item: TreeItem; index: number; level: number; expanded:
boolean; selected: boolean; }`  
`item-label`| `{ item: TreeItem; index: number; level: number; expanded:
boolean; selected: boolean; }`  
`item-trailing`| `{ item: TreeItem; index: number; level: number; expanded:
boolean; selected: boolean; }`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[payload: any]`  
`update:expanded`| `[val: string[]]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        tree: {
          slots: {
            root: 'relative isolate',
            item: '',
            listWithChildren: 'ms-4.5 border-s border-default',
            itemWithChildren: 'ps-1.5 -ms-px',
            link: 'relative group w-full flex items-center text-sm before:absolute before:inset-y-px before:inset-x-0 before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
            linkLeadingIcon: 'shrink-0',
            linkLabel: 'truncate',
            linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
            linkTrailingIcon: 'shrink-0 transform transition-transform duration-200 group-data-expanded:rotate-180'
          },
          variants: {
            color: {
              primary: {
                link: 'focus-visible:before:ring-primary'
              },
              secondary: {
                link: 'focus-visible:before:ring-secondary'
              },
              success: {
                link: 'focus-visible:before:ring-success'
              },
              info: {
                link: 'focus-visible:before:ring-info'
              },
              warning: {
                link: 'focus-visible:before:ring-warning'
              },
              error: {
                link: 'focus-visible:before:ring-error'
              },
              neutral: {
                link: 'focus-visible:before:ring-inverted'
              }
            },
            size: {
              xs: {
                link: 'px-2 py-1 text-xs gap-1',
                linkLeadingIcon: 'size-4',
                linkTrailingIcon: 'size-4'
              },
              sm: {
                link: 'px-2.5 py-1.5 text-xs gap-1.5',
                linkLeadingIcon: 'size-4',
                linkTrailingIcon: 'size-4'
              },
              md: {
                link: 'px-2.5 py-1.5 text-sm gap-1.5',
                linkLeadingIcon: 'size-5',
                linkTrailingIcon: 'size-5'
              },
              lg: {
                link: 'px-3 py-2 text-sm gap-2',
                linkLeadingIcon: 'size-5',
                linkTrailingIcon: 'size-5'
              },
              xl: {
                link: 'px-3 py-2 text-base gap-2',
                linkLeadingIcon: 'size-6',
                linkTrailingIcon: 'size-6'
              }
            },
            selected: {
              true: {
                link: 'before:bg-elevated'
              },
              false: {
                link: [
                  'hover:not-disabled:text-highlighted hover:not-disabled:before:bg-elevated/50',
                  'transition-colors before:transition-colors'
                ]
              }
            },
            disabled: {
              true: {
                link: 'cursor-not-allowed opacity-75'
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              selected: true,
              class: {
                link: 'text-primary'
              }
            },
            {
              color: 'neutral',
              selected: true,
              class: {
                link: 'text-highlighted'
              }
            }
          ],
          defaultVariants: {
            color: 'primary',
            size: 'md'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            tree: {
              slots: {
                root: 'relative isolate',
                item: '',
                listWithChildren: 'ms-4.5 border-s border-default',
                itemWithChildren: 'ps-1.5 -ms-px',
                link: 'relative group w-full flex items-center text-sm before:absolute before:inset-y-px before:inset-x-0 before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
                linkLeadingIcon: 'shrink-0',
                linkLabel: 'truncate',
                linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                linkTrailingIcon: 'shrink-0 transform transition-transform duration-200 group-data-expanded:rotate-180'
              },
              variants: {
                color: {
                  primary: {
                    link: 'focus-visible:before:ring-primary'
                  },
                  secondary: {
                    link: 'focus-visible:before:ring-secondary'
                  },
                  success: {
                    link: 'focus-visible:before:ring-success'
                  },
                  info: {
                    link: 'focus-visible:before:ring-info'
                  },
                  warning: {
                    link: 'focus-visible:before:ring-warning'
                  },
                  error: {
                    link: 'focus-visible:before:ring-error'
                  },
                  neutral: {
                    link: 'focus-visible:before:ring-inverted'
                  }
                },
                size: {
                  xs: {
                    link: 'px-2 py-1 text-xs gap-1',
                    linkLeadingIcon: 'size-4',
                    linkTrailingIcon: 'size-4'
                  },
                  sm: {
                    link: 'px-2.5 py-1.5 text-xs gap-1.5',
                    linkLeadingIcon: 'size-4',
                    linkTrailingIcon: 'size-4'
                  },
                  md: {
                    link: 'px-2.5 py-1.5 text-sm gap-1.5',
                    linkLeadingIcon: 'size-5',
                    linkTrailingIcon: 'size-5'
                  },
                  lg: {
                    link: 'px-3 py-2 text-sm gap-2',
                    linkLeadingIcon: 'size-5',
                    linkTrailingIcon: 'size-5'
                  },
                  xl: {
                    link: 'px-3 py-2 text-base gap-2',
                    linkLeadingIcon: 'size-6',
                    linkTrailingIcon: 'size-6'
                  }
                },
                selected: {
                  true: {
                    link: 'before:bg-elevated'
                  },
                  false: {
                    link: [
                      'hover:not-disabled:text-highlighted hover:not-disabled:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ]
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  selected: true,
                  class: {
                    link: 'text-primary'
                  }
                },
                {
                  color: 'neutral',
                  selected: true,
                  class: {
                    link: 'text-highlighted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            tree: {
              slots: {
                root: 'relative isolate',
                item: '',
                listWithChildren: 'ms-4.5 border-s border-default',
                itemWithChildren: 'ps-1.5 -ms-px',
                link: 'relative group w-full flex items-center text-sm before:absolute before:inset-y-px before:inset-x-0 before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
                linkLeadingIcon: 'shrink-0',
                linkLabel: 'truncate',
                linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                linkTrailingIcon: 'shrink-0 transform transition-transform duration-200 group-data-expanded:rotate-180'
              },
              variants: {
                color: {
                  primary: {
                    link: 'focus-visible:before:ring-primary'
                  },
                  secondary: {
                    link: 'focus-visible:before:ring-secondary'
                  },
                  success: {
                    link: 'focus-visible:before:ring-success'
                  },
                  info: {
                    link: 'focus-visible:before:ring-info'
                  },
                  warning: {
                    link: 'focus-visible:before:ring-warning'
                  },
                  error: {
                    link: 'focus-visible:before:ring-error'
                  },
                  neutral: {
                    link: 'focus-visible:before:ring-inverted'
                  }
                },
                size: {
                  xs: {
                    link: 'px-2 py-1 text-xs gap-1',
                    linkLeadingIcon: 'size-4',
                    linkTrailingIcon: 'size-4'
                  },
                  sm: {
                    link: 'px-2.5 py-1.5 text-xs gap-1.5',
                    linkLeadingIcon: 'size-4',
                    linkTrailingIcon: 'size-4'
                  },
                  md: {
                    link: 'px-2.5 py-1.5 text-sm gap-1.5',
                    linkLeadingIcon: 'size-5',
                    linkTrailingIcon: 'size-5'
                  },
                  lg: {
                    link: 'px-3 py-2 text-sm gap-2',
                    linkLeadingIcon: 'size-5',
                    linkTrailingIcon: 'size-5'
                  },
                  xl: {
                    link: 'px-3 py-2 text-base gap-2',
                    linkLeadingIcon: 'size-6',
                    linkTrailingIcon: 'size-6'
                  }
                },
                selected: {
                  true: {
                    link: 'before:bg-elevated'
                  },
                  false: {
                    link: [
                      'hover:not-disabled:text-highlighted hover:not-disabled:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ]
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  selected: true,
                  class: {
                    link: 'text-primary'
                  }
                },
                {
                  color: 'neutral',
                  selected: true,
                  class: {
                    link: 'text-highlighted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/tree.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[TooltipA popup that reveals information when hovering over an
element.](/components/tooltip)


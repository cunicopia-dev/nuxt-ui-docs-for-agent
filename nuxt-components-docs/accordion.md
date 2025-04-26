<!-- source: https://ui.nuxt.com/components/accordion --> # Accordion

[Accordion](https://reka-
ui.com/docs/components/accordion)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Accordion.vue)

A stacked set of collapsible panels.

## Usage

### Items

Use the `items` prop as an array of objects with the following properties:

  * `label?: string`
  * `icon?: string`
  * `trailingIcon?: string`
  * `content?: string`
  * `value?: string`
  * `disabled?: boolean`
  * `slot?: string`

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = ref<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    </script>
    
    <template>
      <UAccordion :items="items" />
    </template>
    

### Multiple

Set the `type` prop to `multiple` to allow multiple items to be active at the
same time. Defaults to `single`.

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = ref<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    </script>
    
    <template>
      <UAccordion type="multiple" :items="items" />
    </template>
    

### Collapsible

When `type` is `single`, you can set the `collapsible` prop to `false` to
prevent the active item from collapsing.

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = ref<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    </script>
    
    <template>
      <UAccordion :collapsible="false" :items="items" />
    </template>
    

### Unmount

Use the `unmount-on-hide` prop to prevent the content from being unmounted
when the accordion is collapsed. Defaults to `true`.

unmountOnHide

false

Icons

You have nothing to do, @nuxt/icon will handle it automatically.

Colors

Choose a primary and a neutral color from your Tailwind CSS theme.

Components

You can customize components by using the `class` / `ui` props or in your
app.config.ts.

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = ref<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    </script>
    
    <template>
      <UAccordion :unmount-on-hide="false" :items="items" />
    </template>
    

You can inspect the DOM to see each item's content being rendered.

### Disabled

Use the `disabled` property to disable the Accordion.

You can also disable a specific item by using the `disabled` property in the
item object.

disabled

true

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = ref<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.',
        disabled: true
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    </script>
    
    <template>
      <UAccordion disabled :items="items" />
    </template>
    

### Trailing Icon

Use the `trailing-icon` prop to customize the trailing
[Icon](/components/icon) of each item. Defaults to `i-lucide-chevron-down`.

You can also set an icon for a specific item by using the `trailingIcon`
property in the item object.

trailingIcon

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = ref<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.',
        trailingIcon: 'i-lucide-plus'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    </script>
    
    <template>
      <UAccordion trailing-icon="i-lucide-arrow-down" :items="items" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.chevronDown` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.chevronDown` key.

## Examples

### Control active item(s)

You can control the active item(s) by using the `default-value` prop or the
`v-model` directive with the index of the item.

Icons

You have nothing to do, @nuxt/icon will handle it automatically.

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items: AccordionItem[] = [
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ]
    
    const active = ref('0')
    
    // Note: This is for demonstration purposes only. Don't do this at home.
    onMounted(() => {
      setInterval(() => {
        active.value = String((Number(active.value) + 1) % items.length)
      }, 2000)
    })
    </script>
    
    <template>
      <UAccordion v-model="active" :items="items" />
    </template>
    

You can also pass the `value` of one of the items if provided.

When `type="multiple"`, ensure to pass an array to the `default-value` prop or
the `v-model` directive.

### With drag and drop

Use the [`useSortable`](https://vueuse.org/integrations/useSortable/)
composable from
[`@vueuse/integrations`](https://vueuse.org/integrations/README.html) to
enable drag and drop functionality on the Accordion. This integration wraps
[Sortable.js](https://sortablejs.github.io/Sortable/) to provide a seamless
drag and drop experience.

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    import { useSortable } from '@vueuse/integrations/useSortable'
    
    const items = shallowRef<AccordionItem[]>([
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ])
    
    const accordion = useTemplateRef<HTMLElement>('accordion')
    
    useSortable(accordion, items, {
      animation: 150
    })
    </script>
    
    <template>
      <UAccordion ref="accordion" :items="items" />
    </template>
    

### With body slot

Use the `#body` slot to customize the body of each item.

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items: AccordionItem[] = [
      {
        label: 'Icons',
        icon: 'i-lucide-smile'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box'
      }
    ]
    </script>
    
    <template>
      <UAccordion :items="items">
        <template #body="{ item }">
          This is the {{ item.label }} panel.
        </template>
      </UAccordion>
    </template>
    

The `#body` slot includes some pre-defined styles, use the `#content` slot if
you want to start from scratch.

### With content slot

Use the `#content` slot to customize the content of each item.

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items: AccordionItem[] = [
      {
        label: 'Icons',
        icon: 'i-lucide-smile'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box'
      }
    ]
    </script>
    
    <template>
      <UAccordion :items="items">
        <template #content="{ item }">
          <p class="pb-3.5 text-sm text-muted">
            This is the {{ item.label }} panel.
          </p>
        </template>
      </UAccordion>
    </template>
    

### With custom slot

Use the `slot` property to customize a specific item.

You will have access to the following slots:

  * `#{{ item.slot }}`
  * `#{{ item.slot }}-body`

Icons

Colors

Components

    
    
    <script setup lang="ts">
    import type { AccordionItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'Icons',
        icon: 'i-lucide-smile',
        content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
      },
      {
        label: 'Colors',
        icon: 'i-lucide-swatch-book',
        slot: 'colors' as const,
        content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
      }
    ] satisfies AccordionItem[]
    </script>
    
    <template>
      <UAccordion :items="items">
        <template #colors="{ item }">
          <p class="text-sm pb-3.5 text-primary">
            {{ item.content }}
          </p>
        </template>
      </UAccordion>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`items`| | ` AccordionItem[]`Show properties

  * `label?: string`
  * `icon?: string`
  * `trailingIcon?: string`
  * `slot?: string`
  * `content?: string`
  * `value?: string`A unique value for the accordion item. Defaults to the index.
  * `disabled?: boolean`

  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
on the right side of the trigger.  
`labelKey`| `'label'`| ` string`The key used to get the label from the item.  
`collapsible`| `true`| `boolean`When type is "single", allows closing content
when clicking trigger for an open item. When type is "multiple", this prop has
no effect.  
`defaultValue`| | ` string | string[]`The default active value of the item(s).Use when you do not need to control the state of the item(s).  
`modelValue`| | ` string | string[]`The controlled value of the active item(s).Use this when you need to control the state of the items. Can be binded with `v-model`  
`type`| `'single'`| ` "single" | "multiple"`Determines whether a "single" or "multiple" items can be selected at a time.This prop will overwrite the inferred type from `modelValue` and `defaultValue`.  
`disabled`| `false`| `boolean`When `true`, prevents the user from interacting
with the accordion and all its items  
`unmountOnHide`| `true`| `boolean`When `true`, the element will be unmounted
on closed state.  
`ui`| | ` { root?: ClassNameValue; item?: ClassNameValue; header?: ClassNameValue; trigger?: ClassNameValue; content?: ClassNameValue; body?: ClassNameValue; leadingIcon?: ClassNameValue; trailingIcon?: ClassNameValue; label?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{ item: AccordionItem; index: number; open: boolean; }`  
`default`| `{ item: AccordionItem; index: number; open: boolean; }`  
`trailing`| `{ item: AccordionItem; index: number; open: boolean; }`  
`content`| `{ item: AccordionItem; index: number; open: boolean; }`  
`body`| `{ item: AccordionItem; index: number; open: boolean; }`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[value: string | string[] | undefined]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        accordion: {
          slots: {
            root: 'w-full',
            item: 'border-b border-default last:border-b-0',
            header: 'flex',
            trigger: 'group flex-1 flex items-center gap-1.5 font-medium text-sm py-3.5 focus-visible:outline-primary min-w-0',
            content: 'data-[state=open]:animate-[accordion-down_200ms_ease-out] data-[state=closed]:animate-[accordion-up_200ms_ease-out] overflow-hidden focus:outline-none',
            body: 'text-sm pb-3.5',
            leadingIcon: 'shrink-0 size-5',
            trailingIcon: 'shrink-0 size-5 ms-auto group-data-[state=open]:rotate-180 transition-transform duration-200',
            label: 'text-start break-words'
          },
          variants: {
            disabled: {
              true: {
                trigger: 'cursor-not-allowed opacity-75'
              }
            }
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
            accordion: {
              slots: {
                root: 'w-full',
                item: 'border-b border-default last:border-b-0',
                header: 'flex',
                trigger: 'group flex-1 flex items-center gap-1.5 font-medium text-sm py-3.5 focus-visible:outline-primary min-w-0',
                content: 'data-[state=open]:animate-[accordion-down_200ms_ease-out] data-[state=closed]:animate-[accordion-up_200ms_ease-out] overflow-hidden focus:outline-none',
                body: 'text-sm pb-3.5',
                leadingIcon: 'shrink-0 size-5',
                trailingIcon: 'shrink-0 size-5 ms-auto group-data-[state=open]:rotate-180 transition-transform duration-200',
                label: 'text-start break-words'
              },
              variants: {
                disabled: {
                  true: {
                    trigger: 'cursor-not-allowed opacity-75'
                  }
                }
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
            accordion: {
              slots: {
                root: 'w-full',
                item: 'border-b border-default last:border-b-0',
                header: 'flex',
                trigger: 'group flex-1 flex items-center gap-1.5 font-medium text-sm py-3.5 focus-visible:outline-primary min-w-0',
                content: 'data-[state=open]:animate-[accordion-down_200ms_ease-out] data-[state=closed]:animate-[accordion-up_200ms_ease-out] overflow-hidden focus:outline-none',
                body: 'text-sm pb-3.5',
                leadingIcon: 'shrink-0 size-5',
                trailingIcon: 'shrink-0 size-5 ms-auto group-data-[state=open]:rotate-180 transition-transform duration-200',
                label: 'text-start break-words'
              },
              variants: {
                disabled: {
                  true: {
                    trigger: 'cursor-not-allowed opacity-75'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[AppWraps your app to provide global configurations and
more.](/components/app)[AlertA callout to draw user's
attention.](/components/alert)


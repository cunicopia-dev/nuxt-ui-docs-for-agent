<!-- source: https://ui.nuxt.com/components/checkbox-group --> # CheckboxGroup

[CheckboxGroup](https://reka-ui.com/docs/components/checkbox#group-
root)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/CheckboxGroup.vue)

A set of checklist buttons to select multiple option from a list.

## Usage

Use the `v-model` directive to control the value of the CheckboxGroup or the
`default-value` prop to set the initial value when you do not need to control
its state.

### Items

Use the `items` prop as an array of strings or numbers:

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem, CheckboxGroupValue } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    const value = ref<CheckboxGroupValue[]>(['System'])
    </script>
    
    <template>
      <UCheckboxGroup v-model="value" :items="items" />
    </template>
    

You can also pass an array of objects with the following properties:

  * `label?: string`
  * `description?: string`
  * `value?: string`
  * `disabled?: boolean`

System

This is the first option.

Light

This is the second option.

Dark

This is the third option.

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem, CheckboxGroupValue } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>([
      {
        label: 'System',
        description: 'This is the first option.',
        value: 'system'
      },
      {
        label: 'Light',
        description: 'This is the second option.',
        value: 'light'
      },
      {
        label: 'Dark',
        description: 'This is the third option.',
        value: 'dark'
      }
    ])
    const value = ref<CheckboxGroupValue[]>([
      'system'
    ])
    </script>
    
    <template>
      <UCheckboxGroup v-model="value" :items="items" />
    </template>
    

When using objects, you need to reference the `value` property of the object
in the `v-model` directive or the `default-value` prop.

### Value Key

You can change the property that is used to set the value by using the `value-
key` prop. Defaults to `value`.

System

This is the first option.

Light

This is the second option.

Dark

This is the third option.

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem, CheckboxGroupValue } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>([
      {
        label: 'System',
        description: 'This is the first option.',
        id: 'system'
      },
      {
        label: 'Light',
        description: 'This is the second option.',
        id: 'light'
      },
      {
        label: 'Dark',
        description: 'This is the third option.',
        id: 'dark'
      }
    ])
    const value = ref<CheckboxGroupValue[]>([
      'light'
    ])
    </script>
    
    <template>
      <UCheckboxGroup v-model="value" value-key="id" :items="items" />
    </template>
    

### Legend

Use the `legend` prop to set the legend of the CheckboxGroup.

legend

Theme

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup legend="Theme" :default-value="['System']" :items="items" />
    </template>
    

### Color

Use the `color` prop to change the color of the CheckboxGroup.

color

neutral

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup color="neutral" :default-value="['System']" :items="items" />
    </template>
    

### Variant

Use the `variant` prop to change the variant of the CheckboxGroup.

color

primary

variant

card

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup color="primary" variant="card" :default-value="['System']" :items="items" />
    </template>
    

### Size

Use the `size` prop to change the size of the CheckboxGroup.

size

xl

variant

list

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup size="xl" variant="list" :default-value="['System']" :items="items" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the CheckboxGroup.
Defaults to `vertical`.

orientation

horizontal

variant

list

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup
        orientation="horizontal"
        variant="list"
        :default-value="['System']"
        :items="items"
      />
    </template>
    

### Indicator

Use the `indicator` prop to change the position or hide the indicator.
Defaults to `start`.

indicator

end

variant

card

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup indicator="end" variant="card" :default-value="['System']" :items="items" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the CheckboxGroup.

disabled

true

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { CheckboxGroupItem } from '@nuxt/ui'
    
    const items = ref<CheckboxGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <UCheckboxGroup disabled :default-value="['System']" :items="items" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`legend`| | ` string`  
`valueKey`| `'value'`| ` string`When `items` is an array of objects, select
the field to use as the value.  
`labelKey`| `'label'`| ` string`When `items` is an array of objects, select
the field to use as the label.  
`descriptionKey`| `'description'`| ` string`When `items` is an array of
objects, select the field to use as the description.  
`items`| | ` CheckboxGroupItem[]`Show properties

  * `label?: string`
  * `description?: string`
  * `disabled?: boolean`
  * `value?: string`

  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`The orientation the checkbox buttons are laid out.  
`defaultValue`| | ` AcceptableValue[]`The value of the checkbox when it is initially rendered. Use when you do not need to control its value.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the checkboxes  
`loop`| `false`| `boolean`Whether keyboard navigation should loop around  
`modelValue`| | ` AcceptableValue[]`The controlled value of the checkbox. Can be binded with v-model.  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`required`| | `boolean`When `true`, indicates that the user must set the value before the owning form can be submitted.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'list'`| ` "card" | "list"`  
`indicator`| `'start'`| ` "start" | "end" | "hidden"`Position of the indicator.  
`icon`| `appConfig.ui.icons.check`| ` string`The icon displayed when checked.  
`ui`| | ` { root?: ClassNameValue; fieldset?: ClassNameValue; legend?: ClassNameValue; item?: ClassNameValue; } & { root?: ClassNameValue; ... 6 more ...; description?: ClassNameValue; }`Show properties

  * `root?: ClassNameValue`
  * `fieldset?: ClassNameValue`
  * `legend?: ClassNameValue`
  * `item?: ClassNameValue`
  * `container?: ClassNameValue`
  * `base?: ClassNameValue`
  * `indicator?: ClassNameValue`
  * `icon?: ClassNameValue`
  * `wrapper?: ClassNameValue`
  * `label?: ClassNameValue`
  * `description?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`legend`| `{}`  
`label`| `{ item: CheckboxGroupItem & { id: string; }; }`  
`description`| `{ item: CheckboxGroupItem & { id: string; }; }`  
  
### Emits

Event |  Type   
---|---  
`change`| `[payload: Event]`  
`update:modelValue`| `[value: AcceptableValue[]]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        checkboxGroup: {
          slots: {
            root: 'relative',
            fieldset: 'flex gap-x-2',
            legend: 'mb-1 block font-medium text-default',
            item: ''
          },
          variants: {
            orientation: {
              horizontal: {
                fieldset: 'flex-row'
              },
              vertical: {
                fieldset: 'flex-col'
              }
            },
            size: {
              xs: {
                fieldset: 'gap-y-0.5',
                legend: 'text-xs'
              },
              sm: {
                fieldset: 'gap-y-0.5',
                legend: 'text-xs'
              },
              md: {
                fieldset: 'gap-y-1',
                legend: 'text-sm'
              },
              lg: {
                fieldset: 'gap-y-1',
                legend: 'text-sm'
              },
              xl: {
                fieldset: 'gap-y-1.5',
                legend: 'text-base'
              }
            },
            required: {
              true: {
                legend: "after:content-['*'] after:ms-0.5 after:text-error"
              }
            }
          },
          defaultVariants: {
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
            checkboxGroup: {
              slots: {
                root: 'relative',
                fieldset: 'flex gap-x-2',
                legend: 'mb-1 block font-medium text-default',
                item: ''
              },
              variants: {
                orientation: {
                  horizontal: {
                    fieldset: 'flex-row'
                  },
                  vertical: {
                    fieldset: 'flex-col'
                  }
                },
                size: {
                  xs: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs'
                  },
                  sm: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs'
                  },
                  md: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm'
                  },
                  lg: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm'
                  },
                  xl: {
                    fieldset: 'gap-y-1.5',
                    legend: 'text-base'
                  }
                },
                required: {
                  true: {
                    legend: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                }
              },
              defaultVariants: {
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
            checkboxGroup: {
              slots: {
                root: 'relative',
                fieldset: 'flex gap-x-2',
                legend: 'mb-1 block font-medium text-default',
                item: ''
              },
              variants: {
                orientation: {
                  horizontal: {
                    fieldset: 'flex-row'
                  },
                  vertical: {
                    fieldset: 'flex-col'
                  }
                },
                size: {
                  xs: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs'
                  },
                  sm: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs'
                  },
                  md: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm'
                  },
                  lg: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm'
                  },
                  xl: {
                    fieldset: 'gap-y-1.5',
                    legend: 'text-base'
                  }
                },
                required: {
                  true: {
                    legend: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                }
              },
              defaultVariants: {
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[CheckboxAn input element to toggle between checked and unchecked
states.](/components/checkbox)[ChipAn indicator of a numeric value or a
state.](/components/chip)


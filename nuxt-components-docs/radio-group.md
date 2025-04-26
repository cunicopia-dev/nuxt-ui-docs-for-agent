<!-- source: https://ui.nuxt.com/components/radio-group --> # RadioGroup

[RadioGroup](https://reka-ui.com/docs/components/radio-
group)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/RadioGroup.vue)

A set of radio buttons to select a single option from a list.

## Usage

Use the `v-model` directive to control the value of the RadioGroup or the
`default-value` prop to set the initial value when you do not need to control
its state.

### Items

Use the `items` prop as an array of strings or numbers:

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { RadioGroupItem, RadioGroupValue } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    const value = ref<RadioGroupValue>('System')
    </script>
    
    <template>
      <URadioGroup v-model="value" :items="items" />
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
    import type { RadioGroupItem, RadioGroupValue } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>([
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
    const value = ref<RadioGroupValue>('system')
    </script>
    
    <template>
      <URadioGroup v-model="value" :items="items" />
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
    import type { RadioGroupItem, RadioGroupValue } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>([
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
    const value = ref<RadioGroupValue>('light')
    </script>
    
    <template>
      <URadioGroup v-model="value" value-key="id" :items="items" />
    </template>
    

### Legend

Use the `legend` prop to set the legend of the RadioGroup.

legend

Theme

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <URadioGroup legend="Theme" default-value="System" :items="items" />
    </template>
    

### Color

Use the `color` prop to change the color of the RadioGroup.

color

neutral

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <URadioGroup color="neutral" default-value="System" :items="items" />
    </template>
    

### Variant New

Use the `variant` prop to change the variant of the RadioGroup.

color

primary

variant

table

Pro

Tailored for indie hackers, freelancers and solo founders.

Startup

Best suited for small teams, startups and agencies.

Enterprise

Ideal for larger teams and organizations.

    
    
    <script setup lang="ts">
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>([
      {
        label: 'Pro',
        value: 'pro',
        description: 'Tailored for indie hackers, freelancers and solo founders.'
      },
      {
        label: 'Startup',
        value: 'startup',
        description: 'Best suited for small teams, startups and agencies.'
      },
      {
        label: 'Enterprise',
        value: 'enterprise',
        description: 'Ideal for larger teams and organizations.'
      }
    ])
    </script>
    
    <template>
      <URadioGroup color="primary" variant="table" default-value="pro" :items="items" />
    </template>
    

### Size

Use the `size` prop to change the size of the RadioGroup.

size

xl

variant

list

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <URadioGroup size="xl" variant="list" default-value="System" :items="items" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the RadioGroup.
Defaults to `vertical`.

orientation

horizontal

variant

list

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <URadioGroup orientation="horizontal" variant="list" default-value="System" :items="items" />
    </template>
    

### Indicator New

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
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <URadioGroup indicator="end" variant="card" default-value="System" :items="items" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the RadioGroup.

disabled

true

System

Light

Dark

    
    
    <script setup lang="ts">
    import type { RadioGroupItem } from '@nuxt/ui'
    
    const items = ref<RadioGroupItem[]>(['System', 'Light', 'Dark'])
    </script>
    
    <template>
      <URadioGroup disabled default-value="System" :items="items" />
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
`items`| | ` RadioGroupItem[]`Show properties

  * `label?: string`
  * `description?: string`
  * `disabled?: boolean`
  * `value?: string`

  
`size`| `'md'`| ` "xs" | "sm" | "md" | "lg" | "xl"`  
`variant`| `'list'`| ` "card" | "list" | "table"`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`The orientation the radio buttons are laid out.  
`indicator`| `'start'`| ` "start" | "end" | "hidden"`Position of the indicator.  
`defaultValue`| | ` null | string | number | Record<string, any>`The value of the radio item that should be checked when initially rendered.Use when you do not need to control the state of the radio items.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with radio items.  
`loop`| | `boolean`When `true`, keyboard navigation will loop from last item to first, and vice versa.  
`modelValue`| | ` null | string | number | Record<string, any>`The controlled value of the radio item to check. Can be binded as `v-model`.  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`required`| | `boolean`When `true`, indicates that the user must set the value before the owning form can be submitted.  
`ui`| | ` { root?: ClassNameValue; fieldset?: ClassNameValue; legend?: ClassNameValue; item?: ClassNameValue; container?: ClassNameValue; ... 4 more ...; description?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`legend`| `{}`  
`label`| `{ item: RadioGroupItem & { id: string; }; modelValue?: AcceptableValue | undefined; }`  
`description`| `{ item: RadioGroupItem & { id: string; }; modelValue?: AcceptableValue | undefined; }`  
  
### Emits

Event |  Type   
---|---  
`change`| `[payload: Event]`  
`update:modelValue`| `[payload: string]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        radioGroup: {
          slots: {
            root: 'relative',
            fieldset: 'flex gap-x-2',
            legend: 'mb-1 block font-medium text-default',
            item: 'flex items-start',
            container: 'flex items-center',
            base: 'rounded-full ring ring-inset ring-accented overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-2',
            indicator: 'flex items-center justify-center size-full after:bg-default after:rounded-full',
            wrapper: 'w-full',
            label: 'block font-medium text-default',
            description: 'text-muted'
          },
          variants: {
            color: {
              primary: {
                base: 'focus-visible:outline-primary',
                indicator: 'bg-primary'
              },
              secondary: {
                base: 'focus-visible:outline-secondary',
                indicator: 'bg-secondary'
              },
              success: {
                base: 'focus-visible:outline-success',
                indicator: 'bg-success'
              },
              info: {
                base: 'focus-visible:outline-info',
                indicator: 'bg-info'
              },
              warning: {
                base: 'focus-visible:outline-warning',
                indicator: 'bg-warning'
              },
              error: {
                base: 'focus-visible:outline-error',
                indicator: 'bg-error'
              },
              neutral: {
                base: 'focus-visible:outline-inverted',
                indicator: 'bg-inverted'
              }
            },
            variant: {
              list: {
                item: ''
              },
              card: {
                item: 'border border-muted rounded-lg'
              },
              table: {
                item: 'border border-muted'
              }
            },
            orientation: {
              horizontal: {
                fieldset: 'flex-row'
              },
              vertical: {
                fieldset: 'flex-col'
              }
            },
            indicator: {
              start: {
                item: 'flex-row',
                wrapper: 'ms-2'
              },
              end: {
                item: 'flex-row-reverse',
                wrapper: 'me-2'
              },
              hidden: {
                base: 'sr-only',
                wrapper: 'text-center'
              }
            },
            size: {
              xs: {
                fieldset: 'gap-y-0.5',
                legend: 'text-xs',
                base: 'size-3',
                item: 'text-xs',
                container: 'h-4',
                indicator: 'after:size-1'
              },
              sm: {
                fieldset: 'gap-y-0.5',
                legend: 'text-xs',
                base: 'size-3.5',
                item: 'text-xs',
                container: 'h-4',
                indicator: 'after:size-1'
              },
              md: {
                fieldset: 'gap-y-1',
                legend: 'text-sm',
                base: 'size-4',
                item: 'text-sm',
                container: 'h-5',
                indicator: 'after:size-1.5'
              },
              lg: {
                fieldset: 'gap-y-1',
                legend: 'text-sm',
                base: 'size-4.5',
                item: 'text-sm',
                container: 'h-5',
                indicator: 'after:size-1.5'
              },
              xl: {
                fieldset: 'gap-y-1.5',
                legend: 'text-base',
                base: 'size-5',
                item: 'text-base',
                container: 'h-6',
                indicator: 'after:size-2'
              }
            },
            disabled: {
              true: {
                base: 'cursor-not-allowed opacity-75',
                label: 'cursor-not-allowed opacity-75'
              }
            },
            required: {
              true: {
                legend: "after:content-['*'] after:ms-0.5 after:text-error"
              }
            }
          },
          compoundVariants: [
            {
              size: 'xs',
              variant: [
                'card',
                'table'
              ],
              class: {
                item: 'p-2.5'
              }
            },
            {
              size: 'sm',
              variant: [
                'card',
                'table'
              ],
              class: {
                item: 'p-3'
              }
            },
            {
              size: 'md',
              variant: [
                'card',
                'table'
              ],
              class: {
                item: 'p-3.5'
              }
            },
            {
              size: 'lg',
              variant: [
                'card',
                'table'
              ],
              class: {
                item: 'p-4'
              }
            },
            {
              size: 'xl',
              variant: [
                'card',
                'table'
              ],
              class: {
                item: 'p-4.5'
              }
            },
            {
              orientation: 'horizontal',
              variant: 'table',
              class: {
                item: 'first-of-type:rounded-l-lg last-of-type:rounded-r-lg',
                fieldset: 'gap-0 -space-x-px'
              }
            },
            {
              orientation: 'vertical',
              variant: 'table',
              class: {
                item: 'first-of-type:rounded-t-lg last-of-type:rounded-b-lg',
                fieldset: 'gap-0 -space-y-px'
              }
            },
            {
              color: 'primary',
              variant: 'card',
              class: {
                item: 'has-data-[state=checked]:border-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'card',
              class: {
                item: 'has-data-[state=checked]:border-inverted'
              }
            },
            {
              color: 'primary',
              variant: 'table',
              class: {
                item: 'has-data-[state=checked]:bg-primary/10 has-data-[state=checked]:border-primary/50 has-data-[state=checked]:z-[1]'
              }
            },
            {
              color: 'neutral',
              variant: 'table',
              class: {
                item: 'has-data-[state=checked]:bg-elevated has-data-[state=checked]:border-inverted/50 has-data-[state=checked]:z-[1]'
              }
            },
            {
              variant: [
                'card',
                'table'
              ],
              disabled: true,
              class: {
                item: 'cursor-not-allowed opacity-75'
              }
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary',
            variant: 'list',
            orientation: 'vertical',
            indicator: 'start'
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
            radioGroup: {
              slots: {
                root: 'relative',
                fieldset: 'flex gap-x-2',
                legend: 'mb-1 block font-medium text-default',
                item: 'flex items-start',
                container: 'flex items-center',
                base: 'rounded-full ring ring-inset ring-accented overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-2',
                indicator: 'flex items-center justify-center size-full after:bg-default after:rounded-full',
                wrapper: 'w-full',
                label: 'block font-medium text-default',
                description: 'text-muted'
              },
              variants: {
                color: {
                  primary: {
                    base: 'focus-visible:outline-primary',
                    indicator: 'bg-primary'
                  },
                  secondary: {
                    base: 'focus-visible:outline-secondary',
                    indicator: 'bg-secondary'
                  },
                  success: {
                    base: 'focus-visible:outline-success',
                    indicator: 'bg-success'
                  },
                  info: {
                    base: 'focus-visible:outline-info',
                    indicator: 'bg-info'
                  },
                  warning: {
                    base: 'focus-visible:outline-warning',
                    indicator: 'bg-warning'
                  },
                  error: {
                    base: 'focus-visible:outline-error',
                    indicator: 'bg-error'
                  },
                  neutral: {
                    base: 'focus-visible:outline-inverted',
                    indicator: 'bg-inverted'
                  }
                },
                variant: {
                  list: {
                    item: ''
                  },
                  card: {
                    item: 'border border-muted rounded-lg'
                  },
                  table: {
                    item: 'border border-muted'
                  }
                },
                orientation: {
                  horizontal: {
                    fieldset: 'flex-row'
                  },
                  vertical: {
                    fieldset: 'flex-col'
                  }
                },
                indicator: {
                  start: {
                    item: 'flex-row',
                    wrapper: 'ms-2'
                  },
                  end: {
                    item: 'flex-row-reverse',
                    wrapper: 'me-2'
                  },
                  hidden: {
                    base: 'sr-only',
                    wrapper: 'text-center'
                  }
                },
                size: {
                  xs: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs',
                    base: 'size-3',
                    item: 'text-xs',
                    container: 'h-4',
                    indicator: 'after:size-1'
                  },
                  sm: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs',
                    base: 'size-3.5',
                    item: 'text-xs',
                    container: 'h-4',
                    indicator: 'after:size-1'
                  },
                  md: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm',
                    base: 'size-4',
                    item: 'text-sm',
                    container: 'h-5',
                    indicator: 'after:size-1.5'
                  },
                  lg: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm',
                    base: 'size-4.5',
                    item: 'text-sm',
                    container: 'h-5',
                    indicator: 'after:size-1.5'
                  },
                  xl: {
                    fieldset: 'gap-y-1.5',
                    legend: 'text-base',
                    base: 'size-5',
                    item: 'text-base',
                    container: 'h-6',
                    indicator: 'after:size-2'
                  }
                },
                disabled: {
                  true: {
                    base: 'cursor-not-allowed opacity-75',
                    label: 'cursor-not-allowed opacity-75'
                  }
                },
                required: {
                  true: {
                    legend: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                }
              },
              compoundVariants: [
                {
                  size: 'xs',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-2.5'
                  }
                },
                {
                  size: 'sm',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-3'
                  }
                },
                {
                  size: 'md',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-3.5'
                  }
                },
                {
                  size: 'lg',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-4'
                  }
                },
                {
                  size: 'xl',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-4.5'
                  }
                },
                {
                  orientation: 'horizontal',
                  variant: 'table',
                  class: {
                    item: 'first-of-type:rounded-l-lg last-of-type:rounded-r-lg',
                    fieldset: 'gap-0 -space-x-px'
                  }
                },
                {
                  orientation: 'vertical',
                  variant: 'table',
                  class: {
                    item: 'first-of-type:rounded-t-lg last-of-type:rounded-b-lg',
                    fieldset: 'gap-0 -space-y-px'
                  }
                },
                {
                  color: 'primary',
                  variant: 'card',
                  class: {
                    item: 'has-data-[state=checked]:border-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'card',
                  class: {
                    item: 'has-data-[state=checked]:border-inverted'
                  }
                },
                {
                  color: 'primary',
                  variant: 'table',
                  class: {
                    item: 'has-data-[state=checked]:bg-primary/10 has-data-[state=checked]:border-primary/50 has-data-[state=checked]:z-[1]'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'table',
                  class: {
                    item: 'has-data-[state=checked]:bg-elevated has-data-[state=checked]:border-inverted/50 has-data-[state=checked]:z-[1]'
                  }
                },
                {
                  variant: [
                    'card',
                    'table'
                  ],
                  disabled: true,
                  class: {
                    item: 'cursor-not-allowed opacity-75'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'list',
                orientation: 'vertical',
                indicator: 'start'
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
            radioGroup: {
              slots: {
                root: 'relative',
                fieldset: 'flex gap-x-2',
                legend: 'mb-1 block font-medium text-default',
                item: 'flex items-start',
                container: 'flex items-center',
                base: 'rounded-full ring ring-inset ring-accented overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-2',
                indicator: 'flex items-center justify-center size-full after:bg-default after:rounded-full',
                wrapper: 'w-full',
                label: 'block font-medium text-default',
                description: 'text-muted'
              },
              variants: {
                color: {
                  primary: {
                    base: 'focus-visible:outline-primary',
                    indicator: 'bg-primary'
                  },
                  secondary: {
                    base: 'focus-visible:outline-secondary',
                    indicator: 'bg-secondary'
                  },
                  success: {
                    base: 'focus-visible:outline-success',
                    indicator: 'bg-success'
                  },
                  info: {
                    base: 'focus-visible:outline-info',
                    indicator: 'bg-info'
                  },
                  warning: {
                    base: 'focus-visible:outline-warning',
                    indicator: 'bg-warning'
                  },
                  error: {
                    base: 'focus-visible:outline-error',
                    indicator: 'bg-error'
                  },
                  neutral: {
                    base: 'focus-visible:outline-inverted',
                    indicator: 'bg-inverted'
                  }
                },
                variant: {
                  list: {
                    item: ''
                  },
                  card: {
                    item: 'border border-muted rounded-lg'
                  },
                  table: {
                    item: 'border border-muted'
                  }
                },
                orientation: {
                  horizontal: {
                    fieldset: 'flex-row'
                  },
                  vertical: {
                    fieldset: 'flex-col'
                  }
                },
                indicator: {
                  start: {
                    item: 'flex-row',
                    wrapper: 'ms-2'
                  },
                  end: {
                    item: 'flex-row-reverse',
                    wrapper: 'me-2'
                  },
                  hidden: {
                    base: 'sr-only',
                    wrapper: 'text-center'
                  }
                },
                size: {
                  xs: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs',
                    base: 'size-3',
                    item: 'text-xs',
                    container: 'h-4',
                    indicator: 'after:size-1'
                  },
                  sm: {
                    fieldset: 'gap-y-0.5',
                    legend: 'text-xs',
                    base: 'size-3.5',
                    item: 'text-xs',
                    container: 'h-4',
                    indicator: 'after:size-1'
                  },
                  md: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm',
                    base: 'size-4',
                    item: 'text-sm',
                    container: 'h-5',
                    indicator: 'after:size-1.5'
                  },
                  lg: {
                    fieldset: 'gap-y-1',
                    legend: 'text-sm',
                    base: 'size-4.5',
                    item: 'text-sm',
                    container: 'h-5',
                    indicator: 'after:size-1.5'
                  },
                  xl: {
                    fieldset: 'gap-y-1.5',
                    legend: 'text-base',
                    base: 'size-5',
                    item: 'text-base',
                    container: 'h-6',
                    indicator: 'after:size-2'
                  }
                },
                disabled: {
                  true: {
                    base: 'cursor-not-allowed opacity-75',
                    label: 'cursor-not-allowed opacity-75'
                  }
                },
                required: {
                  true: {
                    legend: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                }
              },
              compoundVariants: [
                {
                  size: 'xs',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-2.5'
                  }
                },
                {
                  size: 'sm',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-3'
                  }
                },
                {
                  size: 'md',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-3.5'
                  }
                },
                {
                  size: 'lg',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-4'
                  }
                },
                {
                  size: 'xl',
                  variant: [
                    'card',
                    'table'
                  ],
                  class: {
                    item: 'p-4.5'
                  }
                },
                {
                  orientation: 'horizontal',
                  variant: 'table',
                  class: {
                    item: 'first-of-type:rounded-l-lg last-of-type:rounded-r-lg',
                    fieldset: 'gap-0 -space-x-px'
                  }
                },
                {
                  orientation: 'vertical',
                  variant: 'table',
                  class: {
                    item: 'first-of-type:rounded-t-lg last-of-type:rounded-b-lg',
                    fieldset: 'gap-0 -space-y-px'
                  }
                },
                {
                  color: 'primary',
                  variant: 'card',
                  class: {
                    item: 'has-data-[state=checked]:border-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'card',
                  class: {
                    item: 'has-data-[state=checked]:border-inverted'
                  }
                },
                {
                  color: 'primary',
                  variant: 'table',
                  class: {
                    item: 'has-data-[state=checked]:bg-primary/10 has-data-[state=checked]:border-primary/50 has-data-[state=checked]:z-[1]'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'table',
                  class: {
                    item: 'has-data-[state=checked]:bg-elevated has-data-[state=checked]:border-inverted/50 has-data-[state=checked]:z-[1]'
                  }
                },
                {
                  variant: [
                    'card',
                    'table'
                  ],
                  disabled: true,
                  class: {
                    item: 'cursor-not-allowed opacity-75'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'list',
                orientation: 'vertical',
                indicator: 'start'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/radio-group.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[ProgressAn indicator showing the progress of a
task.](/components/progress)[SelectA select element to choose from a list of
options.](/components/select)


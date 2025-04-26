<!-- source: https://ui.nuxt.com/components/checkbox --> # Checkbox

[Checkbox](https://reka-
ui.com/docs/components/checkbox)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Checkbox.vue)

An input element to toggle between checked and unchecked states.

## Usage

Use the `v-model` directive to control the checked state of the Checkbox.

    
    
    <script setup lang="ts">
    const value = ref(true)
    </script>
    
    <template>
      <UCheckbox v-model="value" />
    </template>
    

Use the `default-value` prop to set the initial value when you do not need to
control its state.

    
    
    <template>
      <UCheckbox default-value />
    </template>
    

### Indeterminate

Use the `indeterminate` value in the `v-model` directive or `default-value`
prop to set the Checkbox to an [indeterminate
state](https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/input/checkbox#indeterminate_state_checkboxes).

    
    
    <template>
      <UCheckbox default-value="indeterminate" />
    </template>
    

### Indeterminate Icon

Use the `indeterminate-icon` prop to customize the indeterminate icon.
Defaults to `i-lucide-minus`.

indeterminateIcon

    
    
    <template>
      <UCheckbox default-value="indeterminate" indeterminate-icon="i-lucide-plus" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.minus` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.minus` key.

### Label

Use the `label` prop to set the label of the Checkbox.

label

Check me

    
    
    <template>
      <UCheckbox label="Check me" />
    </template>
    

When using the `required` prop, an asterisk is added next to the label.

required

true

Check me

    
    
    <template>
      <UCheckbox required label="Check me" />
    </template>
    

### Description

Use the `description` prop to set the description of the Checkbox.

description

Check me

This is a checkbox.

    
    
    <template>
      <UCheckbox label="Check me" description="This is a checkbox." />
    </template>
    

### Icon

Use the `icon` prop to set the icon of the Checkbox when it is checked.
Defaults to `i-lucide-check`.

icon

Check me

    
    
    <template>
      <UCheckbox icon="i-lucide-heart" default-value label="Check me" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.check` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.check` key.

### Color

Use the `color` prop to change the color of the Checkbox.

color

neutral

Check me

    
    
    <template>
      <UCheckbox color="neutral" default-value label="Check me" />
    </template>
    

### Variant New

Use the `variant` prop to change the variant of the Checkbox.

color

primary

variant

card

Check me

    
    
    <template>
      <UCheckbox color="primary" variant="card" default-value label="Check me" />
    </template>
    

### Size

Use the `size` prop to change the size of the Checkbox.

size

xl

variant

list

Check me

    
    
    <template>
      <UCheckbox size="xl" variant="list" default-value label="Check me" />
    </template>
    

### Indicator New

Use the `indicator` prop to change the position or hide the indicator.
Defaults to `start`.

indicator

end

variant

card

Check me

    
    
    <template>
      <UCheckbox indicator="end" variant="card" default-value label="Check me" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the Checkbox.

disabled

true

Check me

    
    
    <template>
      <UCheckbox disabled label="Check me" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`label`| | ` string`  
`description`| | ` string`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'list'`| ` "card" | "list"`  
`size`| `'md'`| ` "xs" | "sm" | "md" | "lg" | "xl"`  
`indicator`| `'start'`| ` "start" | "end" | "hidden"`Position of the indicator.  
`icon`| `appConfig.ui.icons.check`| ` string`The icon displayed when checked.  
`indeterminateIcon`| `appConfig.ui.icons.minus`| ` string`The icon displayed
when the checkbox is indeterminate.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the checkbox  
`value`| `"on"`| ` null | string | number | Record<string, any>`The value given as data when submitted with a `name`.  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`required`| | `boolean`When `true`, indicates that the user must set the value before the owning form can be submitted.  
`id`| | ` string`Id of the element  
`defaultValue`| | `boolean | "indeterminate"`The value of the checkbox when it is initially rendered. Use when you do not need to control its value.  
`modelValue`| `undefined`| `boolean | "indeterminate"`  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; base?: ClassNameValue; indicator?: ClassNameValue; icon?: ClassNameValue; wrapper?: ClassNameValue; label?: ClassNameValue; description?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`label`| `{ label?: string | undefined; }`  
`description`| `{ description?: string | undefined; }`  
  
### Emits

Event |  Type   
---|---  
`change`| `[payload: Event]`  
`update:modelValue`| `[value: boolean | "indeterminate"]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        checkbox: {
          slots: {
            root: 'relative flex items-start',
            container: 'flex items-center',
            base: 'rounded-sm ring ring-inset ring-accented overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-2',
            indicator: 'flex items-center justify-center size-full text-inverted',
            icon: 'shrink-0 size-full',
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
                root: ''
              },
              card: {
                root: 'border border-muted rounded-lg'
              }
            },
            indicator: {
              start: {
                root: 'flex-row',
                wrapper: 'ms-2'
              },
              end: {
                root: 'flex-row-reverse',
                wrapper: 'me-2'
              },
              hidden: {
                base: 'sr-only',
                wrapper: 'text-center'
              }
            },
            size: {
              xs: {
                base: 'size-3',
                container: 'h-4',
                wrapper: 'text-xs'
              },
              sm: {
                base: 'size-3.5',
                container: 'h-4',
                wrapper: 'text-xs'
              },
              md: {
                base: 'size-4',
                container: 'h-5',
                wrapper: 'text-sm'
              },
              lg: {
                base: 'size-4.5',
                container: 'h-5',
                wrapper: 'text-sm'
              },
              xl: {
                base: 'size-5',
                container: 'h-6',
                wrapper: 'text-base'
              }
            },
            required: {
              true: {
                label: "after:content-['*'] after:ms-0.5 after:text-error"
              }
            },
            disabled: {
              true: {
                base: 'cursor-not-allowed opacity-75',
                label: 'cursor-not-allowed opacity-75',
                description: 'cursor-not-allowed opacity-75'
              }
            },
            checked: {
              true: ''
            }
          },
          compoundVariants: [
            {
              size: 'xs',
              variant: 'card',
              class: {
                root: 'p-2.5'
              }
            },
            {
              size: 'sm',
              variant: 'card',
              class: {
                root: 'p-3'
              }
            },
            {
              size: 'md',
              variant: 'card',
              class: {
                root: 'p-3.5'
              }
            },
            {
              size: 'lg',
              variant: 'card',
              class: {
                root: 'p-4'
              }
            },
            {
              size: 'xl',
              variant: 'card',
              class: {
                root: 'p-4.5'
              }
            },
            {
              color: 'primary',
              variant: 'card',
              class: {
                root: 'has-data-[state=checked]:border-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'card',
              class: {
                root: 'has-data-[state=checked]:border-inverted'
              }
            },
            {
              variant: 'card',
              disabled: true,
              class: {
                root: 'cursor-not-allowed opacity-75'
              }
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary',
            variant: 'list',
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
            checkbox: {
              slots: {
                root: 'relative flex items-start',
                container: 'flex items-center',
                base: 'rounded-sm ring ring-inset ring-accented overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-2',
                indicator: 'flex items-center justify-center size-full text-inverted',
                icon: 'shrink-0 size-full',
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
                    root: ''
                  },
                  card: {
                    root: 'border border-muted rounded-lg'
                  }
                },
                indicator: {
                  start: {
                    root: 'flex-row',
                    wrapper: 'ms-2'
                  },
                  end: {
                    root: 'flex-row-reverse',
                    wrapper: 'me-2'
                  },
                  hidden: {
                    base: 'sr-only',
                    wrapper: 'text-center'
                  }
                },
                size: {
                  xs: {
                    base: 'size-3',
                    container: 'h-4',
                    wrapper: 'text-xs'
                  },
                  sm: {
                    base: 'size-3.5',
                    container: 'h-4',
                    wrapper: 'text-xs'
                  },
                  md: {
                    base: 'size-4',
                    container: 'h-5',
                    wrapper: 'text-sm'
                  },
                  lg: {
                    base: 'size-4.5',
                    container: 'h-5',
                    wrapper: 'text-sm'
                  },
                  xl: {
                    base: 'size-5',
                    container: 'h-6',
                    wrapper: 'text-base'
                  }
                },
                required: {
                  true: {
                    label: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                },
                disabled: {
                  true: {
                    base: 'cursor-not-allowed opacity-75',
                    label: 'cursor-not-allowed opacity-75',
                    description: 'cursor-not-allowed opacity-75'
                  }
                },
                checked: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  size: 'xs',
                  variant: 'card',
                  class: {
                    root: 'p-2.5'
                  }
                },
                {
                  size: 'sm',
                  variant: 'card',
                  class: {
                    root: 'p-3'
                  }
                },
                {
                  size: 'md',
                  variant: 'card',
                  class: {
                    root: 'p-3.5'
                  }
                },
                {
                  size: 'lg',
                  variant: 'card',
                  class: {
                    root: 'p-4'
                  }
                },
                {
                  size: 'xl',
                  variant: 'card',
                  class: {
                    root: 'p-4.5'
                  }
                },
                {
                  color: 'primary',
                  variant: 'card',
                  class: {
                    root: 'has-data-[state=checked]:border-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'card',
                  class: {
                    root: 'has-data-[state=checked]:border-inverted'
                  }
                },
                {
                  variant: 'card',
                  disabled: true,
                  class: {
                    root: 'cursor-not-allowed opacity-75'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'list',
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
            checkbox: {
              slots: {
                root: 'relative flex items-start',
                container: 'flex items-center',
                base: 'rounded-sm ring ring-inset ring-accented overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-2',
                indicator: 'flex items-center justify-center size-full text-inverted',
                icon: 'shrink-0 size-full',
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
                    root: ''
                  },
                  card: {
                    root: 'border border-muted rounded-lg'
                  }
                },
                indicator: {
                  start: {
                    root: 'flex-row',
                    wrapper: 'ms-2'
                  },
                  end: {
                    root: 'flex-row-reverse',
                    wrapper: 'me-2'
                  },
                  hidden: {
                    base: 'sr-only',
                    wrapper: 'text-center'
                  }
                },
                size: {
                  xs: {
                    base: 'size-3',
                    container: 'h-4',
                    wrapper: 'text-xs'
                  },
                  sm: {
                    base: 'size-3.5',
                    container: 'h-4',
                    wrapper: 'text-xs'
                  },
                  md: {
                    base: 'size-4',
                    container: 'h-5',
                    wrapper: 'text-sm'
                  },
                  lg: {
                    base: 'size-4.5',
                    container: 'h-5',
                    wrapper: 'text-sm'
                  },
                  xl: {
                    base: 'size-5',
                    container: 'h-6',
                    wrapper: 'text-base'
                  }
                },
                required: {
                  true: {
                    label: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                },
                disabled: {
                  true: {
                    base: 'cursor-not-allowed opacity-75',
                    label: 'cursor-not-allowed opacity-75',
                    description: 'cursor-not-allowed opacity-75'
                  }
                },
                checked: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  size: 'xs',
                  variant: 'card',
                  class: {
                    root: 'p-2.5'
                  }
                },
                {
                  size: 'sm',
                  variant: 'card',
                  class: {
                    root: 'p-3'
                  }
                },
                {
                  size: 'md',
                  variant: 'card',
                  class: {
                    root: 'p-3.5'
                  }
                },
                {
                  size: 'lg',
                  variant: 'card',
                  class: {
                    root: 'p-4'
                  }
                },
                {
                  size: 'xl',
                  variant: 'card',
                  class: {
                    root: 'p-4.5'
                  }
                },
                {
                  color: 'primary',
                  variant: 'card',
                  class: {
                    root: 'has-data-[state=checked]:border-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'card',
                  class: {
                    root: 'has-data-[state=checked]:border-inverted'
                  }
                },
                {
                  variant: 'card',
                  disabled: true,
                  class: {
                    root: 'cursor-not-allowed opacity-75'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'list',
                indicator: 'start'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/checkbox.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[CarouselA carousel with motion and swipe built using
Embla.](/components/carousel)[CheckboxGroupA set of checklist buttons to
select multiple option from a list.](/components/checkbox-group)


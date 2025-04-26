<!-- source: https://ui.nuxt.com/components/pin-input --> # PinInput

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/PinInput.vue)

An input element to enter a pin.

## Usage

Use the `v-model` directive to control the value of the PinInput.

    
    
    <script setup lang="ts">
    const value = ref([])
    </script>
    
    <template>
      <UPinInput v-model="value" />
    </template>
    

Use the `default-value` prop to set the initial value when you do not need to
control its state.

    
    
    <template>
      <UPinInput :default-value="['1', '2', '3']" />
    </template>
    

### Type

Use the `type` prop to change the input type. Defaults to `text`.

type

number

    
    
    <template>
      <UPinInput type="number" />
    </template>
    

When `type` is set to `number`, it will only accept numeric characters.

### Mask

Use the `mask` prop to treat the input like a password.

mask

true

    
    
    <template>
      <UPinInput mask :default-value="['1', '2', '3', '4', '5']" />
    </template>
    

### OTP

Use the `otp` prop to enable One-Time Password functionality. When enabled,
mobile devices can automatically detect and fill OTP codes from SMS messages
or clipboard content, with autocomplete support.

otp

true

    
    
    <template>
      <UPinInput otp />
    </template>
    

### Length

Use the `length` prop to change the amount of inputs.

length

    
    
    <template>
      <UPinInput :length="6" />
    </template>
    

### Placeholder

Use the `placeholder` prop to set a placeholder text.

placeholder

    
    
    <template>
      <UPinInput placeholder="○" />
    </template>
    

### Color

Use the `color` prop to change the ring color when the PinInput is focused.

color

neutral

highlight

true

    
    
    <template>
      <UPinInput color="neutral" highlight placeholder="○" />
    </template>
    

The `highlight` prop is used here to show the focus state. It's used
internally when a validation error occurs.

### Variant

Use the `variant` prop to change the variant of the PinInput.

color

neutral

variant

subtle

highlight

false

    
    
    <template>
      <UPinInput color="neutral" variant="subtle" placeholder="○" />
    </template>
    

### Size

Use the `size` prop to change the size of the PinInput.

size

xl

    
    
    <template>
      <UPinInput size="xl" placeholder="○" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the PinInput.

disabled

true

    
    
    <template>
      <UPinInput disabled placeholder="○" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "none"`  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`length`| `5`| ` string | number`The number of input fields.  
`autofocus`| | `boolean`  
`autofocusDelay`| `0`| ` number`  
`highlight`| | `boolean`  
`modelValue`| | ` null | string[]`The controlled checked state of the pin input. Can be binded as `v-model`.  
`defaultValue`| | ` string[]`The default value of the pin inputs when it is initially rendered. Use when you do not need to control its checked state.  
`type`| `'text'`| ` "number" | "text"`Input type for the inputs.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the pin input  
`id`| | ` string`Id of the element  
`mask`| | `boolean`When `true`, pin inputs will be treated as password.  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`otp`| | `boolean`When `true`, mobile devices will autodetect the OTP from messages or clipboard, and enable the autocomplete field.  
`placeholder`| | ` string`The placeholder character to use for empty pin-inputs.  
`required`| | `boolean`When `true`, indicates that the user must set the value before the owning form can be submitted.  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; }`  
  
### Emits

Event |  Type   
---|---  
`blur`| `[payload: Event]`  
`change`| `[payload: Event]`  
`update:modelValue`| `[value: string[]]`  
`complete`| `[value: string[]]`  
  
When accessing the component via a template ref, you can use the following:

Name| Type  
---|---  
`inputsRef`| `Ref<ComponentPublicInstance[]>`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        pinInput: {
          slots: {
            root: 'relative inline-flex items-center gap-1.5',
            base: [
              'rounded-md border-0 placeholder:text-dimmed text-center focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
              'transition-colors'
            ]
          },
          variants: {
            size: {
              xs: {
                base: 'size-6 text-xs'
              },
              sm: {
                base: 'size-7 text-xs'
              },
              md: {
                base: 'size-8 text-sm'
              },
              lg: {
                base: 'size-9 text-sm'
              },
              xl: {
                base: 'size-10 text-base'
              }
            },
            variant: {
              outline: 'text-highlighted bg-default ring ring-inset ring-accented',
              soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
              subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
              ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
              none: 'text-highlighted bg-transparent'
            },
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            highlight: {
              true: ''
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              variant: [
                'outline',
                'subtle'
              ],
              class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
            },
            {
              color: 'primary',
              highlight: true,
              class: 'ring ring-inset ring-primary'
            },
            {
              color: 'neutral',
              variant: [
                'outline',
                'subtle'
              ],
              class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
            },
            {
              color: 'neutral',
              highlight: true,
              class: 'ring ring-inset ring-inverted'
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary',
            variant: 'outline'
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
            pinInput: {
              slots: {
                root: 'relative inline-flex items-center gap-1.5',
                base: [
                  'rounded-md border-0 placeholder:text-dimmed text-center focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ]
              },
              variants: {
                size: {
                  xs: {
                    base: 'size-6 text-xs'
                  },
                  sm: {
                    base: 'size-7 text-xs'
                  },
                  md: {
                    base: 'size-8 text-sm'
                  },
                  lg: {
                    base: 'size-9 text-sm'
                  },
                  xl: {
                    base: 'size-10 text-base'
                  }
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                highlight: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  highlight: true,
                  class: 'ring ring-inset ring-primary'
                },
                {
                  color: 'neutral',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  highlight: true,
                  class: 'ring ring-inset ring-inverted'
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'outline'
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
            pinInput: {
              slots: {
                root: 'relative inline-flex items-center gap-1.5',
                base: [
                  'rounded-md border-0 placeholder:text-dimmed text-center focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ]
              },
              variants: {
                size: {
                  xs: {
                    base: 'size-6 text-xs'
                  },
                  sm: {
                    base: 'size-7 text-xs'
                  },
                  md: {
                    base: 'size-8 text-sm'
                  },
                  lg: {
                    base: 'size-9 text-sm'
                  },
                  xl: {
                    base: 'size-10 text-base'
                  }
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                highlight: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  highlight: true,
                  class: 'ring ring-inset ring-primary'
                },
                {
                  color: 'neutral',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  highlight: true,
                  class: 'ring ring-inset ring-inverted'
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/pin-input.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[PaginationA list of buttons or links to navigate through
pages.](/components/pagination)[PopoverA non-modal dialog that floats around a
trigger element.](/components/popover)


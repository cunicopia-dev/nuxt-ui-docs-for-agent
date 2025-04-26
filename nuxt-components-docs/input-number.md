<!-- source: https://ui.nuxt.com/components/input-number --> # InputNumber

[Number Field](https://www.reka-ui.com/components/input-
number)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/InputNumber.vue)

Input numerical values with a customizable range.

This component relies on the [`@internationalized/number`](https://react-
spectrum.adobe.com/internationalized/number/index.html) package which provides
utilities for formatting and parsing numbers across locales and numbering
systems.

## Usage

Use the `v-model` directive to control the value of the InputNumber.

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" />
    </template>
    

Use the `default-value` prop to set the initial value when you do not need to
control its state.

    
    
    <template>
      <UInputNumber :default-value="5" />
    </template>
    

### Min / Max

Use the `min` and `max` props to set the minimum and maximum values of the
InputNumber.

min

max

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" :min="0" :max="10" />
    </template>
    

### Step

Use the `step` prop to set the step value of the InputNumber.

step

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" :step="2" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the InputNumber.

orientation

vertical

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" orientation="vertical" />
    </template>
    

### Placeholder

Use the `placeholder` prop to set a placeholder text.

placeholder

    
    
    <template>
      <UInputNumber placeholder="Enter a number" />
    </template>
    

### Color

Use the `color` prop to change the ring color when the InputNumber is focused.

color

neutral

highlight

true

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" color="neutral" highlight />
    </template>
    

### Variant

Use the `variant` prop to change the variant of the InputNumber.

variant

subtle

color

neutral

highlight

false

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" variant="subtle" color="neutral" />
    </template>
    

### Size

Use the `size` prop to change the size of the InputNumber.

size

xl

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" size="xl" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the InputNumber.

disabled

true

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value" disabled />
    </template>
    

### Increment / Decrement

Use the `increment` and `decrement` props to customize the increment and
decrement buttons with any [Button](/components/button) props. Defaults to `{
variant: 'link' }`.

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber
        v-model="value"
        :increment="{
          color: 'neutral',
          variant: 'solid',
          size: 'xs'
        }"
        :decrement="{
          color: 'neutral',
          variant: 'solid',
          size: 'xs'
        }"
      />
    </template>
    

### Increment / Decrement Icons

Use the `increment-icon` and `decrement-icon` props to customize the buttons
[Icon](/components/icon). Defaults to `i-lucide-plus` / `i-lucide-minus`.

incrementIcon

decrementIcon

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber
        v-model="value"
        increment-icon="i-lucide-arrow-right"
        decrement-icon="i-lucide-arrow-left"
      />
    </template>
    

## Examples

### With decimal format

Use the `format-options` prop to customize the format of the value.

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber
        v-model="value"
        :format-options="{
          signDisplay: 'exceptZero',
          minimumFractionDigits: 1
        }"
      />
    </template>
    

### With percentage format

Use the `format-options` prop with `style: 'percent'` to customize the format
of the value.

    
    
    <script setup lang="ts">
    const value = ref(0.05)
    </script>
    
    <template>
      <UInputNumber
        v-model="value"
        :step="0.01"
        :format-options="{
          style: 'percent'
        }"
      />
    </template>
    

### With currency format

Use the `format-options` prop with `style: 'currency'` to customize the format
of the value.

    
    
    <script setup lang="ts">
    const value = ref(1500)
    </script>
    
    <template>
      <UInputNumber
        v-model="value"
        :format-options="{
          style: 'currency',
          currency: 'EUR',
          currencyDisplay: 'code',
          currencySign: 'accounting'
        }"
      />
    </template>
    

### Within a FormField

You can use the InputNumber within a [FormField](/components/form-field)
component to display a label, help text, required indicator, etc.

Retries

Specify number of attempts

    
    
    <script setup lang="ts">
    const retries = ref(0)
    </script>
    
    <template>
      <UFormField label="Retries" help="Specify number of attempts" required>
        <UInputNumber v-model="retries" placeholder="Enter retries" />
      </UFormField>
    </template>
    

### With slots

Use the `#increment` and `#decrement` slots to customize the buttons.

    
    
    <script setup lang="ts">
    const value = ref(5)
    </script>
    
    <template>
      <UInputNumber v-model="value">
        <template #decrement>
          <UButton size="xs" icon="i-lucide-minus" />
        </template>
    
        <template #increment>
          <UButton size="xs" icon="i-lucide-plus" />
        </template>
      </UInputNumber>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`placeholder`| | ` string`The placeholder text when the input is empty.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "none"`  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`highlight`| | `boolean`Highlight the ring color like a focus state.  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the input menu.  
`increment`| `{ variant: 'link' }`| ` ButtonProps`Configure the increment
button. The `color` and `size` are inherited.Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "outline" | "soft" | "subtle" | "ghost" | "solid"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "outline" | "soft" | "subtle" | "ghost" | "solid"`
  * `size?: "sm" | "md" | "xs" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: (string & {}) | "_blank" | "_parent" | "_self" | "_top" | null`Where to display the linked URL, as the name for a browsing context.

  
`incrementIcon`| `appConfig.ui.icons.plus`| ` string`The icon displayed to
increment the value.  
`decrement`| `{ variant: 'link' }`| ` ButtonProps`Configure the decrement
button. The `color` and `size` are inherited.Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "outline" | "soft" | "subtle" | "ghost" | "solid"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "outline" | "soft" | "subtle" | "ghost" | "solid"`
  * `size?: "sm" | "md" | "xs" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: (string & {}) | "_blank" | "_parent" | "_self" | "_top" | null`Where to display the linked URL, as the name for a browsing context.

  
`decrementIcon`| `appConfig.ui.icons.minus`| ` string`The icon displayed to
decrement the value.  
`autofocus`| | `boolean`  
`autofocusDelay`| | ` number`  
`locale`| `UApp.locale.code`| ` string`The locale to use for formatting and
parsing numbers.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the Number Field.  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`modelValue`| | ` null | number`  
`defaultValue`| | ` number`  
`required`| | `boolean`When `true`, indicates that the user must set the value before the owning form can be submitted.  
`id`| | ` string`Id of the element  
`min`| | ` number`The smallest value allowed for the input.  
`max`| | ` number`The largest value allowed for the input.  
`step`| | ` number`The amount that the input value changes with each increment or decrement "tick".  
`stepSnapping`| | `boolean`When `false`, prevents the value from snapping to the nearest increment of the step value  
`formatOptions`| | ` NumberFormatOptions`Formatting options for the value displayed in the number field. This also affects what characters are allowed to be typed by the user.  
`disableWheelChange`| | `boolean`When `true`, prevents the value from changing on wheel scroll.  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; increment?: ClassNameValue; decrement?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`increment`| `{}`  
`decrement`| `{}`  
  
### Emits

Event |  Type   
---|---  
`blur`| `[event: FocusEvent]`  
`change`| `[payload: Event]`  
`update:modelValue`| `[payload: number]`  
  
### Expose

When accessing the component via a template ref, you can use the following:

Name| Type  
---|---  
`inputRef`| `Ref<HTMLInputElement | null>`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        inputNumber: {
          slots: {
            root: 'relative inline-flex items-center',
            base: [
              'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
              'transition-colors'
            ],
            increment: 'absolute flex items-center',
            decrement: 'absolute flex items-center'
          },
          variants: {
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            size: {
              xs: 'px-2 py-1 text-xs gap-1',
              sm: 'px-2.5 py-1.5 text-xs gap-1.5',
              md: 'px-2.5 py-1.5 text-sm gap-1.5',
              lg: 'px-3 py-2 text-sm gap-2',
              xl: 'px-3 py-2 text-base gap-2'
            },
            variant: {
              outline: 'text-highlighted bg-default ring ring-inset ring-accented',
              soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
              subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
              ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
              none: 'text-highlighted bg-transparent'
            },
            disabled: {
              true: {
                increment: 'opacity-75 cursor-not-allowed',
                decrement: 'opacity-75 cursor-not-allowed'
              }
            },
            orientation: {
              horizontal: {
                base: 'text-center',
                increment: 'inset-y-0 end-0 pe-1',
                decrement: 'inset-y-0 start-0 ps-1'
              },
              vertical: {
                increment: 'top-0 end-0 pe-1 [&>button]:py-0 scale-80',
                decrement: 'bottom-0 end-0 pe-1 [&>button]:py-0 scale-80'
              }
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
            },
            {
              orientation: 'horizontal',
              size: 'xs',
              class: 'px-7'
            },
            {
              orientation: 'horizontal',
              size: 'sm',
              class: 'px-8'
            },
            {
              orientation: 'horizontal',
              size: 'md',
              class: 'px-9'
            },
            {
              orientation: 'horizontal',
              size: 'lg',
              class: 'px-10'
            },
            {
              orientation: 'horizontal',
              size: 'xl',
              class: 'px-11'
            },
            {
              orientation: 'vertical',
              size: 'xs',
              class: 'pe-7'
            },
            {
              orientation: 'vertical',
              size: 'sm',
              class: 'pe-8'
            },
            {
              orientation: 'vertical',
              size: 'md',
              class: 'pe-9'
            },
            {
              orientation: 'vertical',
              size: 'lg',
              class: 'pe-10'
            },
            {
              orientation: 'vertical',
              size: 'xl',
              class: 'pe-11'
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
            inputNumber: {
              slots: {
                root: 'relative inline-flex items-center',
                base: [
                  'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                increment: 'absolute flex items-center',
                decrement: 'absolute flex items-center'
              },
              variants: {
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                size: {
                  xs: 'px-2 py-1 text-xs gap-1',
                  sm: 'px-2.5 py-1.5 text-xs gap-1.5',
                  md: 'px-2.5 py-1.5 text-sm gap-1.5',
                  lg: 'px-3 py-2 text-sm gap-2',
                  xl: 'px-3 py-2 text-base gap-2'
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                disabled: {
                  true: {
                    increment: 'opacity-75 cursor-not-allowed',
                    decrement: 'opacity-75 cursor-not-allowed'
                  }
                },
                orientation: {
                  horizontal: {
                    base: 'text-center',
                    increment: 'inset-y-0 end-0 pe-1',
                    decrement: 'inset-y-0 start-0 ps-1'
                  },
                  vertical: {
                    increment: 'top-0 end-0 pe-1 [&>button]:py-0 scale-80',
                    decrement: 'bottom-0 end-0 pe-1 [&>button]:py-0 scale-80'
                  }
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
                },
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: 'px-7'
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: 'px-8'
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: 'px-9'
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: 'px-10'
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: 'px-11'
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: 'pe-11'
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
            inputNumber: {
              slots: {
                root: 'relative inline-flex items-center',
                base: [
                  'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                increment: 'absolute flex items-center',
                decrement: 'absolute flex items-center'
              },
              variants: {
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                size: {
                  xs: 'px-2 py-1 text-xs gap-1',
                  sm: 'px-2.5 py-1.5 text-xs gap-1.5',
                  md: 'px-2.5 py-1.5 text-sm gap-1.5',
                  lg: 'px-3 py-2 text-sm gap-2',
                  xl: 'px-3 py-2 text-base gap-2'
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                disabled: {
                  true: {
                    increment: 'opacity-75 cursor-not-allowed',
                    decrement: 'opacity-75 cursor-not-allowed'
                  }
                },
                orientation: {
                  horizontal: {
                    base: 'text-center',
                    increment: 'inset-y-0 end-0 pe-1',
                    decrement: 'inset-y-0 start-0 ps-1'
                  },
                  vertical: {
                    increment: 'top-0 end-0 pe-1 [&>button]:py-0 scale-80',
                    decrement: 'bottom-0 end-0 pe-1 [&>button]:py-0 scale-80'
                  }
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
                },
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: 'px-7'
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: 'px-8'
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: 'px-9'
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: 'px-10'
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: 'px-11'
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: 'pe-11'
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

[](https://github.com/nuxt/ui/blob/v3/src/theme/input-number.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[InputMenuAn autocomplete input with real-time
suggestions.](/components/input-menu)[KbdA kbd element to display a keyboard
key.](/components/kbd)


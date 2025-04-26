<!-- source: https://ui.nuxt.com/components/input --> # Input

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Input.vue)

An input element to enter text.

## Usage

Use the `v-model` directive to control the value of the Input.

    
    
    <script setup lang="ts">
    const value = ref('')
    </script>
    
    <template>
      <UInput v-model="value" />
    </template>
    

### Type

Use the `type` prop to change the input type. Defaults to `text`.

Some types have been implemented in their own components such as
[Checkbox](/components/checkbox), [Radio](/components/radio-group),
[InputNumber](/components/input-number) etc. and others have been styled like
`file` for example.

type

file

    
    
    <template>
      <UInput type="file" />
    </template>
    

[](https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/input#input_types)You can check all the available
types on the MDN Web Docs.

### Placeholder

Use the `placeholder` prop to set a placeholder text.

placeholder

    
    
    <template>
      <UInput placeholder="Search..." />
    </template>
    

### Color

Use the `color` prop to change the ring color when the Input is focused.

color

neutral

highlight

true

    
    
    <template>
      <UInput color="neutral" highlight placeholder="Search..." />
    </template>
    

The `highlight` prop is used here to show the focus state. It's used
internally when a validation error occurs.

### Variant

Use the `variant` prop to change the variant of the Input.

color

neutral

variant

subtle

highlight

false

    
    
    <template>
      <UInput color="neutral" variant="subtle" placeholder="Search..." />
    </template>
    

### Size

Use the `size` prop to change the size of the Input.

size

xl

    
    
    <template>
      <UInput size="xl" placeholder="Search..." />
    </template>
    

### Icon

Use the `icon` prop to show an [Icon](/components/icon) inside the Input.

icon

size

md

variant

outline

    
    
    <template>
      <UInput icon="i-lucide-search" size="md" variant="outline" placeholder="Search..." />
    </template>
    

Use the `leading` and `trailing` props to set the icon position or the
`leading-icon` and `trailing-icon` props to set a different icon for each
position.

trailingIcon

size

md

    
    
    <template>
      <UInput trailing-icon="i-lucide-at-sign" placeholder="Enter your email" size="md" />
    </template>
    

### Avatar

Use the `avatar` prop to show an [Avatar](/components/avatar) inside the
Input.

avatar.src

size

md

variant

outline

![](https://github.com/nuxt.png)

    
    
    <template>
      <UInput
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
        size="md"
        variant="outline"
        placeholder="Search..."
      />
    </template>
    

### Loading

Use the `loading` prop to show a loading icon on the Input.

loading

true

trailing

false

    
    
    <template>
      <UInput loading placeholder="Search..." />
    </template>
    

### Loading Icon

Use the `loading-icon` prop to customize the loading icon. Defaults to
`i-lucide-refresh-cw`.

loading

true

loadingIcon

    
    
    <template>
      <UInput loading loading-icon="i-lucide-repeat-2" placeholder="Search..." />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.loading` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.loading` key.

### Disabled

Use the `disabled` prop to disable the Input.

disabled

true

    
    
    <template>
      <UInput disabled placeholder="Search..." />
    </template>
    

## Examples

### With clear button

You can put a [Button](/components/button) inside the `#trailing` slot to
clear the Input.

    
    
    <script setup lang="ts">
    const value = ref('Click to clear')
    </script>
    
    <template>
      <UInput
        v-model="value"
        placeholder="Type something..."
        :ui="{ trailing: 'pe-1' }"
      >
        <template v-if="value?.length" #trailing>
          <UButton
            color="neutral"
            variant="link"
            size="sm"
            icon="i-lucide-circle-x"
            aria-label="Clear input"
            @click="value = ''"
          />
        </template>
      </UInput>
    </template>
    

### With copy button

You can put a [Button](/components/button) inside the `#trailing` slot to copy
the value to the clipboard.

    
    
    <script setup lang="ts">
    const value = ref('npx nuxi module add ui')
    const copied = ref(false)
    
    function copy() {
      navigator.clipboard.writeText(value.value)
      copied.value = true
    
      setTimeout(() => {
        copied.value = false
      }, 2000)
    }
    </script>
    
    <template>
      <UInput
        v-model="value"
        :ui="{ trailing: 'pr-0.5' }"
      >
        <template v-if="value?.length" #trailing>
          <UTooltip text="Copy to clipboard" :content="{ side: 'right' }">
            <UButton
              :color="copied ? 'success' : 'neutral'"
              variant="link"
              size="sm"
              :icon="copied ? 'i-lucide-copy-check' : 'i-lucide-copy'"
              aria-label="Copy to clipboard"
              @click="copy"
            />
          </UTooltip>
        </template>
      </UInput>
    </template>
    

### With password toggle

You can put a [Button](/components/button) inside the `#trailing` slot to
toggle the password visibility.

    
    
    <script setup lang="ts">
    const show = ref(false)
    const password = ref('')
    </script>
    
    <template>
      <UInput
        v-model="password"
        placeholder="Password"
        :type="show ? 'text' : 'password'"
        :ui="{ trailing: 'pe-1' }"
      >
        <template #trailing>
          <UButton
            color="neutral"
            variant="link"
            size="sm"
            :icon="show ? 'i-lucide-eye-off' : 'i-lucide-eye'"
            :aria-label="show ? 'Hide password' : 'Show password'"
            :aria-pressed="show"
            aria-controls="password"
            @click="show = !show"
          />
        </template>
      </UInput>
    </template>
    

### With password strength indicator

You can use the [Progress](/components/progress) component to display the
password strength indicator.

Password

Enter a password. Must contain:

  * At least 8 characters  \- Requirement not met
  * At least 1 number  \- Requirement not met
  * At least 1 lowercase letter  \- Requirement not met
  * At least 1 uppercase letter  \- Requirement not met

    
    
    <script setup lang="ts">
    const show = ref(false)
    const password = ref('')
    
    function checkStrength(str: string) {
      const requirements = [
        { regex: /.{8,}/, text: 'At least 8 characters' },
        { regex: /\d/, text: 'At least 1 number' },
        { regex: /[a-z]/, text: 'At least 1 lowercase letter' },
        { regex: /[A-Z]/, text: 'At least 1 uppercase letter' }
      ]
    
      return requirements.map(req => ({ met: req.regex.test(str), text: req.text }))
    }
    
    const strength = computed(() => checkStrength(password.value))
    const score = computed(() => strength.value.filter(req => req.met).length)
    
    const color = computed(() => {
      if (score.value === 0) return 'neutral'
      if (score.value <= 1) return 'error'
      if (score.value <= 2) return 'warning'
      if (score.value === 3) return 'warning'
      return 'success'
    })
    
    const text = computed(() => {
      if (score.value === 0) return 'Enter a password'
      if (score.value <= 2) return 'Weak password'
      if (score.value === 3) return 'Medium password'
      return 'Strong password'
    })
    </script>
    
    <template>
      <div class="space-y-2">
        <UFormField label="Password">
          <UInput
            v-model="password"
            placeholder="Password"
            :color="color"
            :type="show ? 'text' : 'password'"
            :ui="{ trailing: 'pe-1' }"
            :aria-invalid="score < 4"
            aria-describedby="password-strength"
            class="w-full"
          >
            <template #trailing>
              <UButton
                color="neutral"
                variant="link"
                size="sm"
                :icon="show ? 'i-lucide-eye-off' : 'i-lucide-eye'"
                :aria-label="show ? 'Hide password' : 'Show password'"
                :aria-pressed="show"
                aria-controls="password"
                @click="show = !show"
              />
            </template>
          </UInput>
        </UFormField>
    
        <UProgress
          :color="color"
          :indicator="text"
          :model-value="score"
          :max="4"
          size="sm"
        />
    
        <p id="password-strength" class="text-sm font-medium">
          {{ text }}. Must contain:
        </p>
    
        <ul class="space-y-1" aria-label="Password requirements">
          <li
            v-for="(req, index) in strength"
            :key="index"
            class="flex items-center gap-0.5"
            :class="req.met ? 'text-success' : 'text-muted'"
          >
            <UIcon :name="req.met ? 'i-lucide-circle-check' : 'i-lucide-circle-x'" class="size-4 shrink-0" />
    
            <span class="text-xs font-light">
              {{ req.text }}
              <span class="sr-only">
                {{ req.met ? ' - Requirement met' : ' - Requirement not met' }}
              </span>
            </span>
          </li>
        </ul>
      </div>
    </template>
    

Expand code

### With character limit

You can use the `#trailing` slot to add a character limit to the Input.

0/15

    
    
    <script setup lang="ts">
    const value = ref('')
    const maxLength = 15
    </script>
    
    <template>
      <UInput
        v-model="value"
        :maxlength="maxLength"
        aria-describedby="character-count"
        :ui="{ trailing: 'pointer-events-none' }"
      >
        <template #trailing>
          <div
            id="character-count"
            class="text-xs text-muted tabular-nums"
            aria-live="polite"
            role="status"
          >
            {{ value?.length }}/{{ maxLength }}
          </div>
        </template>
      </UInput>
    </template>
    

### With keyboard shortcut

You can use the [Kbd](/components/kbd) component inside the `#trailing` slot
to add a keyboard shortcut to the Input.

`/`

    
    
    <script setup lang="ts">
    const input = useTemplateRef('input')
    
    defineShortcuts({
      '/': () => {
        input.value?.inputRef?.focus()
      }
    })
    </script>
    
    <template>
      <UInput
        ref="input"
        icon="i-lucide-search"
        placeholder="Search..."
      >
        <template #trailing>
          <UKbd value="/" />
        </template>
      </UInput>
    </template>
    

[](/composables/define-shortcuts)This example uses the `defineShortcuts`
composable to focus the Input when the `/` key is pressed.

### With floating label

You can use the `#default` slot to add a floating label to the Input.

Email address

    
    
    <script setup lang="ts">
    const value = ref('')
    </script>
    
    <template>
      <UInput v-model="value" placeholder="" :ui="{ base: 'peer' }">
        <label class="pointer-events-none absolute left-0 -top-2.5 text-highlighted text-xs font-medium px-1.5 transition-all peer-focus:-top-2.5 peer-focus:text-highlighted peer-focus:text-xs peer-focus:font-medium peer-placeholder-shown:text-sm peer-placeholder-shown:text-dimmed peer-placeholder-shown:top-1.5 peer-placeholder-shown:font-normal">
          <span class="inline-flex bg-default px-1">Email address</span>
        </label>
      </UInput>
    </template>
    

### Within a FormField

You can use the Input within a [FormField](/components/form-field) component
to display a label, help text, required indicator, etc.

Email

We won't share your email.

    
    
    <script setup lang="ts">
    const email = ref('')
    </script>
    
    <template>
      <UFormField label="Email" help="We won't share your email." required>
        <UInput v-model="email" placeholder="Enter your email" icon="i-lucide-at-sign" />
      </UFormField>
    </template>
    

[](/components/form)It also provides validation and error handling when used
within a **Form** component.

### Within a ButtonGroup

You can use the Input within a [ButtonGroup](/components/button-group)
component to group multiple elements together.

https://

.com

    
    
    <script setup lang="ts">
    const value = ref('')
    const domains = ['.com', '.dev', '.org']
    const domain = ref(domains[0])
    </script>
    
    <template>
      <UButtonGroup>
        <UInput
          v-model="value"
          placeholder="nuxt"
          :ui="{
            base: 'pl-[57px]',
            leading: 'pointer-events-none'
          }"
        >
          <template #leading>
            <p class="text-sm text-muted">
              https://
            </p>
          </template>
        </UInput>
    
        <USelectMenu v-model="domain" :items="domains" />
      </UButtonGroup>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`id`| | ` string`  
`name`| | ` string`  
`type`| `'text'`| ` "number" | "reset" | "submit" | "search" | "date" | "text" | "color" | "button" | "checkbox" | "datetime-local" | "email" | "file" | "hidden" | "image" | "month" | "password" | "radio" | "range" | "tel" | "time" | "url" | "week" | string & {}`  
`placeholder`| | ` string`The placeholder text when the input is empty.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "none"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`required`| | `boolean`  
`autocomplete`| `'off'`| ` string`  
`autofocus`| | `boolean`  
`autofocusDelay`| `0`| ` number`  
`disabled`| | `boolean`  
`highlight`| | `boolean`Highlight the ring color like a focus state.  
`icon`| | ` string`Display an icon based on the `leading` and `trailing` props.  
`avatar`| | ` AvatarProps`Display an avatar on the left side.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl" | "3xs" | "2xs" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`leading`| | `boolean`When `true`, the icon will be displayed on the left side.  
`leadingIcon`| | ` string`Display an icon on the left side.  
`trailing`| | `boolean`When `true`, the icon will be displayed on the right side.  
`trailingIcon`| | ` string`Display an icon on the right side.  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`modelValue`| | ` null | string | number`  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
### Emits

Event |  Type   
---|---  
`blur`| `[event: FocusEvent]`  
`change`| `[event: Event]`  
`update:modelValue`| `[payload: string | number]`  
  
### Expose

When accessing the component via a template ref, you can use the following:

Name| Type  
---|---  
`inputRef`| `Ref<HTMLInputElement | null>`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        input: {
          slots: {
            root: 'relative inline-flex items-center',
            base: [
              'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
              'transition-colors'
            ],
            leading: 'absolute inset-y-0 start-0 flex items-center',
            leadingIcon: 'shrink-0 text-dimmed',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            trailing: 'absolute inset-y-0 end-0 flex items-center',
            trailingIcon: 'shrink-0 text-dimmed'
          },
          variants: {
            buttonGroup: {
              horizontal: {
                root: 'group',
                base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
              },
              vertical: {
                root: 'group',
                base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
              }
            },
            size: {
              xs: {
                base: 'px-2 py-1 text-xs gap-1',
                leading: 'ps-2',
                trailing: 'pe-2',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              sm: {
                base: 'px-2.5 py-1.5 text-xs gap-1.5',
                leading: 'ps-2.5',
                trailing: 'pe-2.5',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              md: {
                base: 'px-2.5 py-1.5 text-sm gap-1.5',
                leading: 'ps-2.5',
                trailing: 'pe-2.5',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              lg: {
                base: 'px-3 py-2 text-sm gap-2',
                leading: 'ps-3',
                trailing: 'pe-3',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              xl: {
                base: 'px-3 py-2 text-base gap-2',
                leading: 'ps-3',
                trailing: 'pe-3',
                leadingIcon: 'size-6',
                leadingAvatarSize: 'xs',
                trailingIcon: 'size-6'
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
            leading: {
              true: ''
            },
            trailing: {
              true: ''
            },
            loading: {
              true: ''
            },
            highlight: {
              true: ''
            },
            type: {
              file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
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
              leading: true,
              size: 'xs',
              class: 'ps-7'
            },
            {
              leading: true,
              size: 'sm',
              class: 'ps-8'
            },
            {
              leading: true,
              size: 'md',
              class: 'ps-9'
            },
            {
              leading: true,
              size: 'lg',
              class: 'ps-10'
            },
            {
              leading: true,
              size: 'xl',
              class: 'ps-11'
            },
            {
              trailing: true,
              size: 'xs',
              class: 'pe-7'
            },
            {
              trailing: true,
              size: 'sm',
              class: 'pe-8'
            },
            {
              trailing: true,
              size: 'md',
              class: 'pe-9'
            },
            {
              trailing: true,
              size: 'lg',
              class: 'pe-10'
            },
            {
              trailing: true,
              size: 'xl',
              class: 'pe-11'
            },
            {
              loading: true,
              leading: true,
              class: {
                leadingIcon: 'animate-spin'
              }
            },
            {
              loading: true,
              leading: false,
              trailing: true,
              class: {
                trailingIcon: 'animate-spin'
              }
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
            input: {
              slots: {
                root: 'relative inline-flex items-center',
                base: [
                  'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                leading: 'absolute inset-y-0 start-0 flex items-center',
                leadingIcon: 'shrink-0 text-dimmed',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailing: 'absolute inset-y-0 end-0 flex items-center',
                trailingIcon: 'shrink-0 text-dimmed'
              },
              variants: {
                buttonGroup: {
                  horizontal: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
                  },
                  vertical: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
                  }
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leading: 'ps-2',
                    trailing: 'pe-2',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6'
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
                leading: {
                  true: ''
                },
                trailing: {
                  true: ''
                },
                loading: {
                  true: ''
                },
                highlight: {
                  true: ''
                },
                type: {
                  file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
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
                  leading: true,
                  size: 'xs',
                  class: 'ps-7'
                },
                {
                  leading: true,
                  size: 'sm',
                  class: 'ps-8'
                },
                {
                  leading: true,
                  size: 'md',
                  class: 'ps-9'
                },
                {
                  leading: true,
                  size: 'lg',
                  class: 'ps-10'
                },
                {
                  leading: true,
                  size: 'xl',
                  class: 'ps-11'
                },
                {
                  trailing: true,
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  trailing: true,
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  trailing: true,
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  trailing: true,
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  trailing: true,
                  size: 'xl',
                  class: 'pe-11'
                },
                {
                  loading: true,
                  leading: true,
                  class: {
                    leadingIcon: 'animate-spin'
                  }
                },
                {
                  loading: true,
                  leading: false,
                  trailing: true,
                  class: {
                    trailingIcon: 'animate-spin'
                  }
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
            input: {
              slots: {
                root: 'relative inline-flex items-center',
                base: [
                  'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                leading: 'absolute inset-y-0 start-0 flex items-center',
                leadingIcon: 'shrink-0 text-dimmed',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailing: 'absolute inset-y-0 end-0 flex items-center',
                trailingIcon: 'shrink-0 text-dimmed'
              },
              variants: {
                buttonGroup: {
                  horizontal: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
                  },
                  vertical: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
                  }
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leading: 'ps-2',
                    trailing: 'pe-2',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leading: 'ps-2.5',
                    trailing: 'pe-2.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leading: 'ps-3',
                    trailing: 'pe-3',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6'
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
                leading: {
                  true: ''
                },
                trailing: {
                  true: ''
                },
                loading: {
                  true: ''
                },
                highlight: {
                  true: ''
                },
                type: {
                  file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
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
                  leading: true,
                  size: 'xs',
                  class: 'ps-7'
                },
                {
                  leading: true,
                  size: 'sm',
                  class: 'ps-8'
                },
                {
                  leading: true,
                  size: 'md',
                  class: 'ps-9'
                },
                {
                  leading: true,
                  size: 'lg',
                  class: 'ps-10'
                },
                {
                  leading: true,
                  size: 'xl',
                  class: 'ps-11'
                },
                {
                  trailing: true,
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  trailing: true,
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  trailing: true,
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  trailing: true,
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  trailing: true,
                  size: 'xl',
                  class: 'pe-11'
                },
                {
                  loading: true,
                  leading: true,
                  class: {
                    leadingIcon: 'animate-spin'
                  }
                },
                {
                  loading: true,
                  leading: false,
                  trailing: true,
                  class: {
                    trailingIcon: 'animate-spin'
                  }
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

[](https://github.com/nuxt/ui/blob/v3/src/theme/input.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[IconA component to display any icon from
Iconify.](/components/icon)[InputMenuAn autocomplete input with real-time
suggestions.](/components/input-menu)


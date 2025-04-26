<!-- source: https://ui.nuxt.com/components/button --> # Button

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Button.vue)

A button element that can act as a link or trigger an action.

## Usage

### Label

Use the default slot to set the label of the Button.

    
    
    <template>
      <UButton>Button</UButton>
    </template>
    

You can achieve the same result by using the `label` prop.

label

    
    
    <template>
      <UButton label="Button" />
    </template>
    

### Color

Use the `color` prop to change the color of the Button.

color

neutral

    
    
    <template>
      <UButton color="neutral">Button</UButton>
    </template>
    

### Variant

Use the `variant` prop to change the variant of the Button.

color

neutral

variant

outline

    
    
    <template>
      <UButton color="neutral" variant="outline">Button</UButton>
    </template>
    

### Size

Use the `size` prop to change the size of the Button.

size

xl

    
    
    <template>
      <UButton size="xl">Button</UButton>
    </template>
    

### Icon

Use the `icon` prop to show an [Icon](/components/icon) inside the Button.

icon

size

md

color

primary

variant

solid

    
    
    <template>
      <UButton icon="i-lucide-rocket" size="md" color="primary" variant="solid">Button</UButton>
    </template>
    

Use the `leading` and `trailing` props to set the icon position or the
`leading-icon` and `trailing-icon` props to set a different icon for each
position.

trailingIcon

size

md

    
    
    <template>
      <UButton trailing-icon="i-lucide-arrow-right" size="md">Button</UButton>
    </template>
    

The `label` as prop or slot is optional so you can use the Button as an icon-
only button.

icon

size

md

color

primary

variant

solid

    
    
    <template>
      <UButton icon="i-lucide-search" size="md" color="primary" variant="solid" />
    </template>
    

### Avatar

Use the `avatar` prop to show an [Avatar](/components/avatar) inside the
Button.

avatar.src

size

md

color

neutral

variant

outline

    
    
    <template>
      <UButton
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
        size="md"
        color="neutral"
        variant="outline"
      >
        Button
      </UButton>
    </template>
    

The `label` as prop or slot is optional so you can use the Button as an
avatar-only button.

avatar.src

size

md

color

neutral

variant

outline

    
    
    <template>
      <UButton
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
        size="md"
        color="neutral"
        variant="outline"
      />
    </template>
    

### Link

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

to

    
    
    <template>
      <UButton to="https://github.com/nuxt/ui" target="_blank">Button</UButton>
    </template>
    

When the Button is a link or when using the `active` prop, you can use the
`active-color` and `active-variant` props to customize the active state.

active

true

activeColor

primary

activeVariant

solid

    
    
    <template>
      <UButton active color="neutral" variant="outline" active-color="primary" active-variant="solid">
        Button
      </UButton>
    </template>
    

You can also use the `active-class` and `inactive-class` props to customize
the active state.

active

true

activeClass

inactiveClass

    
    
    <template>
      <UButton active active-class="font-bold" inactive-class="font-light">Button</UButton>
    </template>
    

You can configure these styles globally in your `app.config.ts` file under the
`ui.button.variants.active` key.

    
    
    export default defineAppConfig({
      ui: {
        button: {
          variants: {
            active: {
              true: {
                base: 'font-bold'
              }
            }
          }
        }
      }
    })
    

### Loading

Use the `loading` prop to show a loading icon and disable the Button.

loading

true

trailing

false

    
    
    <template>
      <UButton loading>Button</UButton>
    </template>
    

Use the `loading-auto` prop to show the loading icon automatically while the
`@click` promise is pending.

Button

    
    
    <script setup lang="ts">
    async function onClick() {
      return new Promise<void>(res => setTimeout(res, 1000))
    }
    </script>
    
    <template>
      <UButton loading-auto @click="onClick">
        Button
      </UButton>
    </template>
    

This also works with the [Form](/components/form) component.

Full name

Submit

    
    
    <script setup lang="ts">
    const state = reactive({ fullName: '' })
    
    async function onSubmit() {
      return new Promise<void>(res => setTimeout(res, 1000))
    }
    
    async function validate(data: Partial<typeof state>) {
      if (!data.fullName?.length) return [{ name: 'fullName', message: 'Required' }]
      return []
    }
    </script>
    
    <template>
      <UForm :state="state" :validate="validate" @submit="onSubmit">
        <UFormField name="fullName" label="Full name">
          <UInput v-model="state.fullName" />
        </UFormField>
        <UButton type="submit" class="mt-2" loading-auto>
          Submit
        </UButton>
      </UForm>
    </template>
    

### Loading Icon

Use the `loading-icon` prop to customize the loading icon. Defaults to
`i-lucide-refresh-cw`.

loading

true

loadingIcon

    
    
    <template>
      <UButton loading loading-icon="i-lucide-repeat-2">Button</UButton>
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.loading` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.loading` key.

### Disabled

Use the `disabled` prop to disable the Button.

disabled

true

    
    
    <template>
      <UButton disabled>Button</UButton>
    </template>
    

## Examples

### `class` prop

Use the `class` prop to override the base styles of the Button.

class

    
    
    <template>
      <UButton class="font-bold rounded-full">Button</UButton>
    </template>
    

### `ui` prop

Use the `ui` prop to override the slots styles of the Button.

ui.leadingIcon

    
    
    <template>
      <UButton
        icon="i-lucide-rocket"
        color="neutral"
        variant="outline"
        :ui="{
          leadingIcon: 'text-primary'
        }"
      >
        Button
      </UButton>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'button'`| `any`The element or component this component should render
as when not a link.  
`label`| | ` string`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`activeColor`| | ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'solid'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`activeVariant`| | ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`square`| | `boolean`Render the button with equal padding on all sides.  
`block`| | `boolean`Render the button full width.  
`loadingAuto`| | `boolean`Set loading state automatically based on the `@click` promise state  
`icon`| | ` string`Display an icon based on the `leading` and `trailing` props.  
`avatar`| | ` AvatarProps`Display an avatar on the left side.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "2xs" | "md" | "3xs" | "xs" | "sm" | "lg" | "xl" | "2xl" | "3xl"`Defaults to `'md'`.
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
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.Show properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`type`| `'button'`| ` "reset" | "submit" | "button"`The type of the button when not a link.  
`disabled`| | `boolean`  
`active`| `undefined`| `boolean`Force the link to be active independent of the
current route.  
`target`| | ` null | "_blank" | "_parent" | "_self" | "_top" | string & {}`Where to display the linked URL, as the name for a browsing context.  
`ui`| | ` { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`  
  
[](https://github.com/nuxt/ui/blob/v3/src/runtime/components/Link.vue#L13)The
`Button` component extends the `Link` component. Check out the source code on
GitHub.

### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        button: {
          slots: {
            base: [
              'rounded-md font-medium inline-flex items-center disabled:cursor-not-allowed aria-disabled:cursor-not-allowed disabled:opacity-75 aria-disabled:opacity-75',
              'transition-colors'
            ],
            label: 'truncate',
            leadingIcon: 'shrink-0',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            trailingIcon: 'shrink-0'
          },
          variants: {
            buttonGroup: {
              horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
              vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
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
            variant: {
              solid: '',
              outline: '',
              soft: '',
              subtle: '',
              ghost: '',
              link: ''
            },
            size: {
              xs: {
                base: 'px-2 py-1 text-xs gap-1',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              sm: {
                base: 'px-2.5 py-1.5 text-xs gap-1.5',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              md: {
                base: 'px-2.5 py-1.5 text-sm gap-1.5',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              lg: {
                base: 'px-3 py-2 text-sm gap-2',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              xl: {
                base: 'px-3 py-2 text-base gap-2',
                leadingIcon: 'size-6',
                leadingAvatarSize: 'xs',
                trailingIcon: 'size-6'
              }
            },
            block: {
              true: {
                base: 'w-full justify-center',
                trailingIcon: 'ms-auto'
              }
            },
            square: {
              true: ''
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
            active: {
              true: {
                base: ''
              },
              false: {
                base: ''
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              variant: 'solid',
              class: 'text-inverted bg-primary hover:bg-primary/75 disabled:bg-primary aria-disabled:bg-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary'
            },
            {
              color: 'primary',
              variant: 'outline',
              class: 'ring ring-inset ring-primary/50 text-primary hover:bg-primary/10 disabled:bg-transparent aria-disabled:bg-transparent dark:disabled:bg-transparent dark:aria-disabled:bg-transparent focus:outline-none focus-visible:ring-2 focus-visible:ring-primary'
            },
            {
              color: 'primary',
              variant: 'soft',
              class: 'text-primary bg-primary/10 hover:bg-primary/15 focus:outline-none focus-visible:bg-primary/15 disabled:bg-primary/10 aria-disabled:bg-primary/10'
            },
            {
              color: 'primary',
              variant: 'subtle',
              class: 'text-primary ring ring-inset ring-primary/25 bg-primary/10 hover:bg-primary/15 disabled:bg-primary/10 aria-disabled:bg-primary/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary'
            },
            {
              color: 'primary',
              variant: 'ghost',
              class: 'text-primary hover:bg-primary/10 focus:outline-none focus-visible:bg-primary/10 disabled:bg-transparent aria-disabled:bg-transparent dark:disabled:bg-transparent dark:aria-disabled:bg-transparent'
            },
            {
              color: 'primary',
              variant: 'link',
              class: 'text-primary hover:text-primary/75 disabled:text-primary aria-disabled:text-primary focus:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
            },
            {
              color: 'neutral',
              variant: 'solid',
              class: 'text-inverted bg-inverted hover:bg-inverted/90 disabled:bg-inverted aria-disabled:bg-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-inverted'
            },
            {
              color: 'neutral',
              variant: 'outline',
              class: 'ring ring-inset ring-accented text-default bg-default hover:bg-elevated disabled:bg-default aria-disabled:bg-default focus:outline-none focus-visible:ring-2 focus-visible:ring-inverted'
            },
            {
              color: 'neutral',
              variant: 'soft',
              class: 'text-default bg-elevated hover:bg-accented/75 focus:outline-none focus-visible:bg-accented/75 disabled:bg-elevated aria-disabled:bg-elevated'
            },
            {
              color: 'neutral',
              variant: 'subtle',
              class: 'ring ring-inset ring-accented text-default bg-elevated hover:bg-accented/75 disabled:bg-elevated aria-disabled:bg-elevated focus:outline-none focus-visible:ring-2 focus-visible:ring-inverted'
            },
            {
              color: 'neutral',
              variant: 'ghost',
              class: 'text-default hover:bg-elevated focus:outline-none focus-visible:bg-elevated hover:disabled:bg-transparent dark:hover:disabled:bg-transparent hover:aria-disabled:bg-transparent dark:hover:aria-disabled:bg-transparent'
            },
            {
              color: 'neutral',
              variant: 'link',
              class: 'text-muted hover:text-default disabled:text-muted aria-disabled:text-muted focus:outline-none focus-visible:ring-inset focus-visible:ring-2 focus-visible:ring-inverted'
            },
            {
              size: 'xs',
              square: true,
              class: 'p-1'
            },
            {
              size: 'sm',
              square: true,
              class: 'p-1.5'
            },
            {
              size: 'md',
              square: true,
              class: 'p-1.5'
            },
            {
              size: 'lg',
              square: true,
              class: 'p-2'
            },
            {
              size: 'xl',
              square: true,
              class: 'p-2'
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
            color: 'primary',
            variant: 'solid',
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
            button: {
              slots: {
                base: [
                  'rounded-md font-medium inline-flex items-center disabled:cursor-not-allowed aria-disabled:cursor-not-allowed disabled:opacity-75 aria-disabled:opacity-75',
                  'transition-colors'
                ],
                label: 'truncate',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailingIcon: 'shrink-0'
              },
              variants: {
                buttonGroup: {
                  horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
                  vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
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
                variant: {
                  solid: '',
                  outline: '',
                  soft: '',
                  subtle: '',
                  ghost: '',
                  link: ''
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6'
                  }
                },
                block: {
                  true: {
                    base: 'w-full justify-center',
                    trailingIcon: 'ms-auto'
                  }
                },
                square: {
                  true: ''
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
                active: {
                  true: {
                    base: ''
                  },
                  false: {
                    base: ''
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: 'solid',
                  class: 'text-inverted bg-primary hover:bg-primary/75 disabled:bg-primary aria-disabled:bg-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary'
                },
                {
                  color: 'primary',
                  variant: 'outline',
                  class: 'ring ring-inset ring-primary/50 text-primary hover:bg-primary/10 disabled:bg-transparent aria-disabled:bg-transparent dark:disabled:bg-transparent dark:aria-disabled:bg-transparent focus:outline-none focus-visible:ring-2 focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  variant: 'soft',
                  class: 'text-primary bg-primary/10 hover:bg-primary/15 focus:outline-none focus-visible:bg-primary/15 disabled:bg-primary/10 aria-disabled:bg-primary/10'
                },
                {
                  color: 'primary',
                  variant: 'subtle',
                  class: 'text-primary ring ring-inset ring-primary/25 bg-primary/10 hover:bg-primary/15 disabled:bg-primary/10 aria-disabled:bg-primary/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  variant: 'ghost',
                  class: 'text-primary hover:bg-primary/10 focus:outline-none focus-visible:bg-primary/10 disabled:bg-transparent aria-disabled:bg-transparent dark:disabled:bg-transparent dark:aria-disabled:bg-transparent'
                },
                {
                  color: 'primary',
                  variant: 'link',
                  class: 'text-primary hover:text-primary/75 disabled:text-primary aria-disabled:text-primary focus:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'neutral',
                  variant: 'solid',
                  class: 'text-inverted bg-inverted hover:bg-inverted/90 disabled:bg-inverted aria-disabled:bg-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'outline',
                  class: 'ring ring-inset ring-accented text-default bg-default hover:bg-elevated disabled:bg-default aria-disabled:bg-default focus:outline-none focus-visible:ring-2 focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'soft',
                  class: 'text-default bg-elevated hover:bg-accented/75 focus:outline-none focus-visible:bg-accented/75 disabled:bg-elevated aria-disabled:bg-elevated'
                },
                {
                  color: 'neutral',
                  variant: 'subtle',
                  class: 'ring ring-inset ring-accented text-default bg-elevated hover:bg-accented/75 disabled:bg-elevated aria-disabled:bg-elevated focus:outline-none focus-visible:ring-2 focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'ghost',
                  class: 'text-default hover:bg-elevated focus:outline-none focus-visible:bg-elevated hover:disabled:bg-transparent dark:hover:disabled:bg-transparent hover:aria-disabled:bg-transparent dark:hover:aria-disabled:bg-transparent'
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  class: 'text-muted hover:text-default disabled:text-muted aria-disabled:text-muted focus:outline-none focus-visible:ring-inset focus-visible:ring-2 focus-visible:ring-inverted'
                },
                {
                  size: 'xs',
                  square: true,
                  class: 'p-1'
                },
                {
                  size: 'sm',
                  square: true,
                  class: 'p-1.5'
                },
                {
                  size: 'md',
                  square: true,
                  class: 'p-1.5'
                },
                {
                  size: 'lg',
                  square: true,
                  class: 'p-2'
                },
                {
                  size: 'xl',
                  square: true,
                  class: 'p-2'
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
                color: 'primary',
                variant: 'solid',
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
            button: {
              slots: {
                base: [
                  'rounded-md font-medium inline-flex items-center disabled:cursor-not-allowed aria-disabled:cursor-not-allowed disabled:opacity-75 aria-disabled:opacity-75',
                  'transition-colors'
                ],
                label: 'truncate',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailingIcon: 'shrink-0'
              },
              variants: {
                buttonGroup: {
                  horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
                  vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
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
                variant: {
                  solid: '',
                  outline: '',
                  soft: '',
                  subtle: '',
                  ghost: '',
                  link: ''
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6'
                  }
                },
                block: {
                  true: {
                    base: 'w-full justify-center',
                    trailingIcon: 'ms-auto'
                  }
                },
                square: {
                  true: ''
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
                active: {
                  true: {
                    base: ''
                  },
                  false: {
                    base: ''
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: 'solid',
                  class: 'text-inverted bg-primary hover:bg-primary/75 disabled:bg-primary aria-disabled:bg-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary'
                },
                {
                  color: 'primary',
                  variant: 'outline',
                  class: 'ring ring-inset ring-primary/50 text-primary hover:bg-primary/10 disabled:bg-transparent aria-disabled:bg-transparent dark:disabled:bg-transparent dark:aria-disabled:bg-transparent focus:outline-none focus-visible:ring-2 focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  variant: 'soft',
                  class: 'text-primary bg-primary/10 hover:bg-primary/15 focus:outline-none focus-visible:bg-primary/15 disabled:bg-primary/10 aria-disabled:bg-primary/10'
                },
                {
                  color: 'primary',
                  variant: 'subtle',
                  class: 'text-primary ring ring-inset ring-primary/25 bg-primary/10 hover:bg-primary/15 disabled:bg-primary/10 aria-disabled:bg-primary/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  variant: 'ghost',
                  class: 'text-primary hover:bg-primary/10 focus:outline-none focus-visible:bg-primary/10 disabled:bg-transparent aria-disabled:bg-transparent dark:disabled:bg-transparent dark:aria-disabled:bg-transparent'
                },
                {
                  color: 'primary',
                  variant: 'link',
                  class: 'text-primary hover:text-primary/75 disabled:text-primary aria-disabled:text-primary focus:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'neutral',
                  variant: 'solid',
                  class: 'text-inverted bg-inverted hover:bg-inverted/90 disabled:bg-inverted aria-disabled:bg-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'outline',
                  class: 'ring ring-inset ring-accented text-default bg-default hover:bg-elevated disabled:bg-default aria-disabled:bg-default focus:outline-none focus-visible:ring-2 focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'soft',
                  class: 'text-default bg-elevated hover:bg-accented/75 focus:outline-none focus-visible:bg-accented/75 disabled:bg-elevated aria-disabled:bg-elevated'
                },
                {
                  color: 'neutral',
                  variant: 'subtle',
                  class: 'ring ring-inset ring-accented text-default bg-elevated hover:bg-accented/75 disabled:bg-elevated aria-disabled:bg-elevated focus:outline-none focus-visible:ring-2 focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'ghost',
                  class: 'text-default hover:bg-elevated focus:outline-none focus-visible:bg-elevated hover:disabled:bg-transparent dark:hover:disabled:bg-transparent hover:aria-disabled:bg-transparent dark:hover:aria-disabled:bg-transparent'
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  class: 'text-muted hover:text-default disabled:text-muted aria-disabled:text-muted focus:outline-none focus-visible:ring-inset focus-visible:ring-2 focus-visible:ring-inverted'
                },
                {
                  size: 'xs',
                  square: true,
                  class: 'p-1'
                },
                {
                  size: 'sm',
                  square: true,
                  class: 'p-1.5'
                },
                {
                  size: 'md',
                  square: true,
                  class: 'p-1.5'
                },
                {
                  size: 'lg',
                  square: true,
                  class: 'p-2'
                },
                {
                  size: 'xl',
                  square: true,
                  class: 'p-2'
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
                color: 'primary',
                variant: 'solid',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/button.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[BreadcrumbA hierarchy of links to navigate through a
website.](/components/breadcrumb)[ButtonGroupGroup multiple button-like
elements together.](/components/button-group)


<!-- source: https://ui.nuxt.com/components/alert --> # Alert

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Alert.vue)

A callout to draw user's attention.

## Usage

### Title

Use the `title` prop to set the title of the Alert.

title

Heads up!

    
    
    <template>
      <UAlert title="Heads up!" />
    </template>
    

### Description

Use the `description` prop to set the description of the Alert.

title

description

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert title="Heads up!" description="You can change the primary color in your app config." />
    </template>
    

### Icon

Use the `icon` prop to show an [Icon](/components/icon).

icon

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        icon="i-lucide-terminal"
      />
    </template>
    

### Avatar

Use the `avatar` prop to show an [Avatar](/components/avatar).

avatar.src

![](https://github.com/nuxt.png)

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
      />
    </template>
    

### Color

Use the `color` prop to change the color of the Alert.

color

neutral

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        color="neutral"
        title="Heads up!"
        description="You can change the primary color in your app config."
        icon="i-lucide-terminal"
      />
    </template>
    

### Variant

Use the `variant` prop to change the variant of the Alert.

color

neutral

variant

subtle

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        color="neutral"
        variant="subtle"
        title="Heads up!"
        description="You can change the primary color in your app config."
        icon="i-lucide-terminal"
      />
    </template>
    

### Close

Use the `close` prop to display a [Button](/components/button) to dismiss the
Alert.

An `update:open` event will be emitted when the close button is clicked.

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        color="neutral"
        variant="outline"
        close
      />
    </template>
    

You can pass any property from the [Button](/components/button) component to
customize it.

close.class

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        color="neutral"
        variant="outline"
        :close="{
          color: 'primary',
          variant: 'outline',
          class: 'rounded-full'
        }"
      />
    </template>
    

### Close Icon

Use the `close-icon` prop to customize the close button
[Icon](/components/icon). Defaults to `i-lucide-x`.

closeIcon

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        color="neutral"
        variant="outline"
        close
        close-icon="i-lucide-arrow-right"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.close` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.close` key.

### Actions

Use the `actions` prop to add some [Button](/components/button) actions to the
Alert.

description

Heads up!

You can change the primary color in your app config.

Action 1Action 2

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        color="neutral"
        variant="outline"
        :actions="[
          {
            label: 'Action 1'
          },
          {
            label: 'Action 2',
            color: 'neutral',
            variant: 'subtle'
          }
        ]"
      />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Alert.

description

orientation

horizontal

Heads up!

You can change the primary color in your app config.

Action 1Action 2

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        color="neutral"
        variant="outline"
        orientation="horizontal"
        :actions="[
          {
            label: 'Action 1'
          },
          {
            label: 'Action 2',
            color: 'neutral',
            variant: 'subtle'
          }
        ]"
      />
    </template>
    

## Examples

### `class` prop

Use the `class` prop to override the base styles of the Alert.

class

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        class="rounded-none"
      />
    </template>
    

### `ui` prop

Use the `ui` prop to override the slots styles of the Alert.

ui.icon

Heads up!

You can change the primary color in your app config.

    
    
    <template>
      <UAlert
        title="Heads up!"
        description="You can change the primary color in your app config."
        icon="i-lucide-rocket"
        :ui="{
          icon: 'size-11'
        }"
      />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`title`| | ` string`  
`description`| | ` string`  
`icon`| | ` string`  
`avatar`| | ` AvatarProps`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "2xl" | "md" | "3xs" | "2xs" | "xs" | "sm" | "lg" | "xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'solid'`| ` "solid" | "outline" | "soft" | "subtle"`  
`orientation`| `'vertical'`| ` "vertical" | "horizontal"`The orientation between the content and the actions.  
`actions`| | ` ButtonProps[]`Display a list of actions:

  * under the title and description when orientation is `vertical`
  * next to the close button when orientation is `horizontal``{ size: 'xs' }`

Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
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
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`close`| `false`| `boolean | Partial<ButtonProps>`Display a close button to dismiss the alert. `{ size: 'md', color: 'neutral', variant: 'link' }`  
`closeIcon`| `appConfig.ui.icons.close`| ` string`The icon displayed in the
close button.  
`ui`| | ` { root?: ClassNameValue; wrapper?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; icon?: ClassNameValue; avatar?: ClassNameValue; avatarSize?: ClassNameValue; actions?: ClassNameValue; close?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`title`| `{}`  
`description`| `{}`  
`actions`| `{}`  
`close`| `{ ui: { root: (props?: Record<string, any> | undefined) => string; wrapper: (props?: Record<string, any> | undefined) => string; title: (props?: Record<string, any> | undefined) => string; ... 5 more ...; close: (props?: Record<...> | undefined) => string; }; }`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[value: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        alert: {
          slots: {
            root: 'relative overflow-hidden w-full rounded-lg p-4 flex gap-2.5',
            wrapper: 'min-w-0 flex-1 flex flex-col',
            title: 'text-sm font-medium',
            description: 'text-sm opacity-90',
            icon: 'shrink-0 size-5',
            avatar: 'shrink-0',
            avatarSize: '2xl',
            actions: 'flex flex-wrap gap-1.5 shrink-0',
            close: 'p-0'
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
            variant: {
              solid: '',
              outline: '',
              soft: '',
              subtle: ''
            },
            orientation: {
              horizontal: {
                root: 'items-center',
                actions: 'items-center'
              },
              vertical: {
                root: 'items-start',
                actions: 'items-start mt-2.5'
              }
            },
            title: {
              true: {
                description: 'mt-1'
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              variant: 'solid',
              class: {
                root: 'bg-primary text-inverted'
              }
            },
            {
              color: 'primary',
              variant: 'outline',
              class: {
                root: 'text-primary ring ring-inset ring-primary/25'
              }
            },
            {
              color: 'primary',
              variant: 'soft',
              class: {
                root: 'bg-primary/10 text-primary'
              }
            },
            {
              color: 'primary',
              variant: 'subtle',
              class: {
                root: 'bg-primary/10 text-primary ring ring-inset ring-primary/25'
              }
            },
            {
              color: 'neutral',
              variant: 'solid',
              class: {
                root: 'text-inverted bg-inverted'
              }
            },
            {
              color: 'neutral',
              variant: 'outline',
              class: {
                root: 'text-highlighted bg-default ring ring-inset ring-default'
              }
            },
            {
              color: 'neutral',
              variant: 'soft',
              class: {
                root: 'text-highlighted bg-elevated/50'
              }
            },
            {
              color: 'neutral',
              variant: 'subtle',
              class: {
                root: 'text-highlighted bg-elevated/50 ring ring-inset ring-accented'
              }
            }
          ],
          defaultVariants: {
            color: 'primary',
            variant: 'solid'
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
            alert: {
              slots: {
                root: 'relative overflow-hidden w-full rounded-lg p-4 flex gap-2.5',
                wrapper: 'min-w-0 flex-1 flex flex-col',
                title: 'text-sm font-medium',
                description: 'text-sm opacity-90',
                icon: 'shrink-0 size-5',
                avatar: 'shrink-0',
                avatarSize: '2xl',
                actions: 'flex flex-wrap gap-1.5 shrink-0',
                close: 'p-0'
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
                variant: {
                  solid: '',
                  outline: '',
                  soft: '',
                  subtle: ''
                },
                orientation: {
                  horizontal: {
                    root: 'items-center',
                    actions: 'items-center'
                  },
                  vertical: {
                    root: 'items-start',
                    actions: 'items-start mt-2.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-1'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: 'solid',
                  class: {
                    root: 'bg-primary text-inverted'
                  }
                },
                {
                  color: 'primary',
                  variant: 'outline',
                  class: {
                    root: 'text-primary ring ring-inset ring-primary/25'
                  }
                },
                {
                  color: 'primary',
                  variant: 'soft',
                  class: {
                    root: 'bg-primary/10 text-primary'
                  }
                },
                {
                  color: 'primary',
                  variant: 'subtle',
                  class: {
                    root: 'bg-primary/10 text-primary ring ring-inset ring-primary/25'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'solid',
                  class: {
                    root: 'text-inverted bg-inverted'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'outline',
                  class: {
                    root: 'text-highlighted bg-default ring ring-inset ring-default'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'soft',
                  class: {
                    root: 'text-highlighted bg-elevated/50'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'subtle',
                  class: {
                    root: 'text-highlighted bg-elevated/50 ring ring-inset ring-accented'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                variant: 'solid'
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
            alert: {
              slots: {
                root: 'relative overflow-hidden w-full rounded-lg p-4 flex gap-2.5',
                wrapper: 'min-w-0 flex-1 flex flex-col',
                title: 'text-sm font-medium',
                description: 'text-sm opacity-90',
                icon: 'shrink-0 size-5',
                avatar: 'shrink-0',
                avatarSize: '2xl',
                actions: 'flex flex-wrap gap-1.5 shrink-0',
                close: 'p-0'
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
                variant: {
                  solid: '',
                  outline: '',
                  soft: '',
                  subtle: ''
                },
                orientation: {
                  horizontal: {
                    root: 'items-center',
                    actions: 'items-center'
                  },
                  vertical: {
                    root: 'items-start',
                    actions: 'items-start mt-2.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-1'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: 'solid',
                  class: {
                    root: 'bg-primary text-inverted'
                  }
                },
                {
                  color: 'primary',
                  variant: 'outline',
                  class: {
                    root: 'text-primary ring ring-inset ring-primary/25'
                  }
                },
                {
                  color: 'primary',
                  variant: 'soft',
                  class: {
                    root: 'bg-primary/10 text-primary'
                  }
                },
                {
                  color: 'primary',
                  variant: 'subtle',
                  class: {
                    root: 'bg-primary/10 text-primary ring ring-inset ring-primary/25'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'solid',
                  class: {
                    root: 'text-inverted bg-inverted'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'outline',
                  class: {
                    root: 'text-highlighted bg-default ring ring-inset ring-default'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'soft',
                  class: {
                    root: 'text-highlighted bg-elevated/50'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'subtle',
                  class: {
                    root: 'text-highlighted bg-elevated/50 ring ring-inset ring-accented'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                variant: 'solid'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/alert.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[AccordionA stacked set of collapsible
panels.](/components/accordion)[AvatarAn img element with fallback and Nuxt
Image support.](/components/avatar)


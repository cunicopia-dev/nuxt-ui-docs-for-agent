<!-- source: https://ui.nuxt.com/components/toast --> # Toast

[Toast](https://reka-
ui.com/docs/components/toast)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Toast.vue)

A succinct message to provide information or feedback to the user.

## Usage

Use the [useToast](/composables/use-toast) composable to display a toast in
your application.

Make sure to wrap your app with the [`App`](/components/app) component which
uses our
[`Toaster`](https://github.com/nuxt/ui/blob/v3/src/runtime/components/Toaster.vue)
component which uses the [`ToastProvider`](https://reka-
ui.com/docs/components/toast#provider) component from Reka UI.

[](/components/app#props)You can check the `App` component `toaster` prop to
see how to configure the Toaster globally.

### Title

Pass a `title` field to the `toast.add` method to display a title.

title

Show toast

    
    
    <script setup lang="ts">
    const props = defineProps<{
      title: string
    }>()
    
    const toast = useToast()
    
    function showToast() {
      toast.add(props)
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Description

Pass a `description` field to the `toast.add` method to display a description.

title

description

Show toast

    
    
    <script setup lang="ts">
    const props = defineProps<{
      title: string
      description: string
    }>()
    
    const toast = useToast()
    
    function showToast() {
      toast.add(props)
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Icon

Pass an `icon` field to the `toast.add` method to display an
[Icon](/components/icon).

icon

Show toast

    
    
    <script setup lang="ts">
    const props = defineProps<{
      icon: string
    }>()
    
    const toast = useToast()
    
    function showToast() {
      toast.add({
        title: 'Uh oh! Something went wrong.',
        description: 'There was a problem with your request.',
        icon: props.icon
      })
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Avatar

Pass an `avatar` field to the `toast.add` method to display an
[Avatar](/components/avatar).

avatar.src

Invite user

    
    
    <script setup lang="ts">
    import type { AvatarProps } from '@nuxt/ui'
    
    const props = defineProps<{
      avatar: AvatarProps
    }>()
    
    const toast = useToast()
    
    function showToast() {
      toast.add({
        title: 'User invited',
        description: 'benjamincanac was invited to the team.',
        avatar: props.avatar
      })
    }
    </script>
    
    <template>
      <UButton label="Invite user" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Color

Pass a `color` field to the `toast.add` method to change the color of the
Toast.

color

neutral

Show toast

    
    
    <script setup lang="ts">
    import type { ToastProps } from '@nuxt/ui'
    
    const props = defineProps<{
      color: ToastProps['color']
    }>()
    
    const toast = useToast()
    
    function showToast() {
      toast.add({
        title: 'Uh oh! Something went wrong.',
        description: 'There was a problem with your request.',
        icon: 'i-lucide-wifi',
        color: props.color
      })
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Close

Pass a `close` field to customize or hide the close button (with `false`
value).

Show toast

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    function showToast() {
      toast.add({
        title: 'Uh oh! Something went wrong.',
        description: 'There was a problem with your request.',
        icon: 'i-lucide-wifi',
        close: {
          color: 'primary',
          variant: 'outline',
          class: 'rounded-full'
        }
      })
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Close Icon

Pass a `closeIcon` field to customize the close button
[Icon](/components/icon). Default to `i-lucide-x`.

closeIcon

Show toast

    
    
    <script setup lang="ts">
    const props = defineProps<{
      closeIcon: string
    }>()
    
    const toast = useToast()
    
    function showToast() {
      toast.add({
        title: 'Uh oh! Something went wrong.',
        description: 'There was a problem with your request.',
        closeIcon: props.closeIcon
      })
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.close` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.close` key.

### Actions

Pass an `actions` field to add some [Button](/components/button) actions to
the Alert.

description

Show toast

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    const props = defineProps<{
      description: string
    }>()
    
    function showToast() {
      toast.add({
        title: 'Uh oh! Something went wrong.',
        description: props.description,
        actions: [{
          icon: 'i-lucide-refresh-cw',
          label: 'Retry',
          color: 'neutral',
          variant: 'outline',
          onClick: (e) => {
            e?.stopPropagation()
          }
        }]
      })
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Toast.

orientation

horizontal

Show toast

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    const props = defineProps<{
      orientation: 'horizontal' | 'vertical'
    }>()
    
    function showToast() {
      toast.add({
        title: 'Uh oh! Something went wrong.',
        orientation: props.orientation,
        actions: [{
          icon: 'i-lucide-refresh-cw',
          label: 'Retry',
          color: 'neutral',
          variant: 'outline',
          onClick: (e) => {
            e?.stopPropagation()
          }
        }]
      })
    }
    </script>
    
    <template>
      <UButton label="Show toast" color="neutral" variant="outline" @click="showToast" />
    </template>
    

## Examples

### Change global position

Change the `toaster.position` prop on the [App](/components/app#props)
component to change the position of the toasts.

toaster.position

bottom-right

Add to calendar

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    function addToCalendar() {
      const eventDate = new Date(Date.now() + Math.random() * 31536000000)
      const formattedDate = eventDate.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
      })
    
      toast.add({
        title: 'Event added to calendar',
        description: `This event is scheduled for ${formattedDate}.`,
        icon: 'i-lucide-calendar-days'
      })
    }
    </script>
    
    <template>
      <UButton
        label="Add to calendar"
        color="neutral"
        variant="outline"
        icon="i-lucide-plus"
        @click="addToCalendar"
      />
    </template>
    

[](https://github.com/nuxt/ui/blob/v3/docs/app/app.vue#L77)In this example, we
use the `AppConfig` to configure the `position` prop of the `Toaster`
component globally.

### Change global duration

Change the `toaster.duration` prop on the [App](/components/app#props)
component to change the duration of the toasts.

toaster.duration

Add to calendar

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    function addToCalendar() {
      const eventDate = new Date(Date.now() + Math.random() * 31536000000)
      const formattedDate = eventDate.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
      })
    
      toast.add({
        title: 'Event added to calendar',
        description: `This event is scheduled for ${formattedDate}.`,
        icon: 'i-lucide-calendar-days'
      })
    }
    </script>
    
    <template>
      <UButton
        label="Add to calendar"
        color="neutral"
        variant="outline"
        icon="i-lucide-plus"
        @click="addToCalendar"
      />
    </template>
    

[](https://github.com/nuxt/ui/blob/v3/docs/app/app.vue#L77)In this example, we
use the `AppConfig` to configure the `duration` prop of the `Toaster`
component globally.

### Stacked toasts

Set the `toaster.expand` prop to `false` on the [App](/components/app#props)
component to display stacked toasts.

You can hover over the toasts to expand them. This will also pause the timer
of the toasts.

toaster.expand

true

Add to calendar

    
    
    <script setup lang="ts">
    const toast = useToast()
    
    function addToCalendar() {
      const eventDate = new Date(Date.now() + Math.random() * 31536000000)
      const formattedDate = eventDate.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
      })
    
      toast.add({
        title: 'Event added to calendar',
        description: `This event is scheduled for ${formattedDate}.`,
        icon: 'i-lucide-calendar-days'
      })
    }
    </script>
    
    <template>
      <UButton
        label="Add to calendar"
        color="neutral"
        variant="outline"
        icon="i-lucide-plus"
        @click="addToCalendar"
      />
    </template>
    

[](https://github.com/nuxt/ui/blob/v3/docs/app/app.vue#L77)In this example, we
use the `AppConfig` to configure the `expand` prop of the `Toaster` component
globally.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'li'`| `any`The element or component this component should render as.  
`title`| | ` string | VNode<RendererNode, RendererElement, { [key: string]: any; }> | (): VNode<RendererNode, RendererElement, { [key: string]: any; }>`  
`description`| | ` string | VNode<RendererNode, RendererElement, { [key: string]: any; }> | (): VNode<RendererNode, RendererElement, { [key: string]: any; }>`  
`icon`| | ` string`  
`avatar`| | ` AvatarProps`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "3xs" | "2xs" | "xs" | "md" | "sm" | "lg" | "xl" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`The orientation between the content and the actions.  
`actions`| | ` ButtonProps[]`Display a list of actions:

  * under the title and description when orientation is `vertical`
  * next to the close button when orientation is `horizontal``{ size: 'xs' }`

Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "outline" | "soft" | "subtle" | "ghost" | "solid"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "outline" | "soft" | "subtle" | "ghost" | "solid"`
  * `size?: "xs" | "md" | "sm" | "lg" | "xl"`Defaults to `'md'`.
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
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`close`| `true`| `boolean | Partial<ButtonProps>`Display a close button to dismiss the toast. `{ size: 'md', color: 'neutral', variant: 'link' }`  
`closeIcon`| `appConfig.ui.icons.close`| ` string`The icon displayed in the
close button.  
`type`| | ` "foreground" | "background"`Control the sensitivity of the toast for accessibility purposes.For toasts that are the result of a user action, choose `foreground`. Toasts generated from background tasks should use `background`.  
`defaultOpen`| | `boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.  
`open`| | `boolean`The controlled open state of the dialog. Can be bind as `v-model:open`.  
`duration`| | ` number`Time in milliseconds that toast should remain visible for. Overrides value given to `ToastProvider`.  
`ui`| | ` { root?: ClassNameValue; wrapper?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; icon?: ClassNameValue; ... 4 more ...; close?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`title`| `{}`  
`description`| `{}`  
`actions`| `{}`  
`close`| `{ ui: { root: (props?: Record<string, any> | undefined) => string; wrapper: (props?: Record<string, any> | undefined) => string; title: (props?: Record<string, any> | undefined) => string; ... 6 more ...; close: (props?: Record<...> | undefined) => string; }; }`  
  
### Emits

Event |  Type   
---|---  
`pause`| `[]`  
`escapeKeyDown`| `[event: KeyboardEvent]`  
`resume`| `[]`  
`swipeStart`| `[event: SwipeEvent]`  
`swipeMove`| `[event: SwipeEvent]`  
`swipeCancel`| `[event: SwipeEvent]`  
`swipeEnd`| `[event: SwipeEvent]`  
`update:open`| `[value: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        toast: {
          slots: {
            root: 'relative group overflow-hidden bg-default shadow-lg rounded-lg ring ring-default p-4 flex gap-2.5 focus:outline-none',
            wrapper: 'w-0 flex-1 flex flex-col',
            title: 'text-sm font-medium text-highlighted',
            description: 'text-sm text-muted',
            icon: 'shrink-0 size-5',
            avatar: 'shrink-0',
            avatarSize: '2xl',
            actions: 'flex gap-1.5 shrink-0',
            progress: 'absolute inset-x-0 bottom-0 h-1 z-[-1]',
            close: 'p-0'
          },
          variants: {
            color: {
              primary: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary',
                icon: 'text-primary',
                progress: 'bg-primary'
              },
              secondary: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-secondary',
                icon: 'text-secondary',
                progress: 'bg-secondary'
              },
              success: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-success',
                icon: 'text-success',
                progress: 'bg-success'
              },
              info: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-info',
                icon: 'text-info',
                progress: 'bg-info'
              },
              warning: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-warning',
                icon: 'text-warning',
                progress: 'bg-warning'
              },
              error: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-error',
                icon: 'text-error',
                progress: 'bg-error'
              },
              neutral: {
                root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted',
                icon: 'text-highlighted',
                progress: 'bg-inverted'
              }
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
          defaultVariants: {
            color: 'primary'
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
            toast: {
              slots: {
                root: 'relative group overflow-hidden bg-default shadow-lg rounded-lg ring ring-default p-4 flex gap-2.5 focus:outline-none',
                wrapper: 'w-0 flex-1 flex flex-col',
                title: 'text-sm font-medium text-highlighted',
                description: 'text-sm text-muted',
                icon: 'shrink-0 size-5',
                avatar: 'shrink-0',
                avatarSize: '2xl',
                actions: 'flex gap-1.5 shrink-0',
                progress: 'absolute inset-x-0 bottom-0 h-1 z-[-1]',
                close: 'p-0'
              },
              variants: {
                color: {
                  primary: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary',
                    icon: 'text-primary',
                    progress: 'bg-primary'
                  },
                  secondary: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-secondary',
                    icon: 'text-secondary',
                    progress: 'bg-secondary'
                  },
                  success: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-success',
                    icon: 'text-success',
                    progress: 'bg-success'
                  },
                  info: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-info',
                    icon: 'text-info',
                    progress: 'bg-info'
                  },
                  warning: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-warning',
                    icon: 'text-warning',
                    progress: 'bg-warning'
                  },
                  error: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-error',
                    icon: 'text-error',
                    progress: 'bg-error'
                  },
                  neutral: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted',
                    icon: 'text-highlighted',
                    progress: 'bg-inverted'
                  }
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
              defaultVariants: {
                color: 'primary'
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
            toast: {
              slots: {
                root: 'relative group overflow-hidden bg-default shadow-lg rounded-lg ring ring-default p-4 flex gap-2.5 focus:outline-none',
                wrapper: 'w-0 flex-1 flex flex-col',
                title: 'text-sm font-medium text-highlighted',
                description: 'text-sm text-muted',
                icon: 'shrink-0 size-5',
                avatar: 'shrink-0',
                avatarSize: '2xl',
                actions: 'flex gap-1.5 shrink-0',
                progress: 'absolute inset-x-0 bottom-0 h-1 z-[-1]',
                close: 'p-0'
              },
              variants: {
                color: {
                  primary: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary',
                    icon: 'text-primary',
                    progress: 'bg-primary'
                  },
                  secondary: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-secondary',
                    icon: 'text-secondary',
                    progress: 'bg-secondary'
                  },
                  success: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-success',
                    icon: 'text-success',
                    progress: 'bg-success'
                  },
                  info: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-info',
                    icon: 'text-info',
                    progress: 'bg-info'
                  },
                  warning: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-warning',
                    icon: 'text-warning',
                    progress: 'bg-warning'
                  },
                  error: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-error',
                    icon: 'text-error',
                    progress: 'bg-error'
                  },
                  neutral: {
                    root: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted',
                    icon: 'text-highlighted',
                    progress: 'bg-inverted'
                  }
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
              defaultVariants: {
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[TextareaA textarea element to input multi-line
text.](/components/textarea)[TooltipA popup that reveals information when
hovering over an element.](/components/tooltip)


<!-- source: https://ui.nuxt.com/components/banner --> # BannerPRO

[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/Banner.vue)

Display a banner at the top of your website to inform users about important
information.

## Usage

### Title

Use the `title` prop to display a title on the Banner.

title

    
    
    <template>
      <UBanner title="This is a banner with an important message." />
    </template>
    

### Icon

Use the `icon` prop to display an icon on the Banner.

icon

    
    
    <template>
      <UBanner icon="i-lucide-info" title="This is a banner with an icon." />
    </template>
    

### Color

Use the `color` prop to change the color of the Banner.

color

neutral

    
    
    <template>
      <UBanner color="neutral" icon="i-lucide-info" title="This is a banner with an icon." />
    </template>
    

### Close

Use the `close` prop to display a [Button](/components/button) to dismiss the
Banner. Defaults to `false`.

A `close` event will be emitted when the close button is clicked.

    
    
    <template>
      <UBanner id="example" title="This is a closable banner." close />
    </template>
    

When closed, `banner-${id}` will be stored in the local storage to prevent it
from being displayed again.  
For the example above, `banner-example` will be stored in the local storage.

### Close Icon

Use the `close-icon` prop to customize the close button
[Icon](/components/icon). Defaults to `i-lucide-x`.

    
    
    <template>
      <UBanner
        title="This is a closable banner with a custom close icon."
        close
        close-icon="i-lucide-x-circle"
      />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.close` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.close` key.

### Actions

Use the `actions` prop to add some [Button](/components/button) actions to the
Banner.

    
    
    <script setup lang="ts">
    const actions = ref([
      {
        label: 'Action 1',
        variant: 'outline'
      },
      {
        label: 'Action 2',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UBanner title="This is a banner with actions." :actions="actions" />
    </template>
    

The action buttons default to `color="neutral"` and `size="xs"`. You can
customize these values by passing them directly to each action button.

### Link

You can pass any property from the
[`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component such
as `to`, `target`, `rel`, etc.

color

primary

    
    
    <template>
      <UBanner
        to="https://github.com/nuxt/ui-pro"
        target="_blank"
        title="Purchase Nuxt UI Pro and get access to all components."
        color="primary"
      />
    </template>
    

The `NuxtLink` component will inherit all other attributes you pass to the
`User` component.

## Examples

### Within `app.vue`

Use the Banner component in your `app.vue` or in a layout:

app.vue

    
    
    <template>
      <UApp>
        <UBanner icon="i-lucide-construction" title="Nuxt UI v3 has been released!" />
    
        <UHeader />
    
        <UMain>
          <NuxtLayout>
            <NuxtPage />
          </NuxtLayout>
        </UMain>
    
        <UFooter />
      </UApp>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`icon`| | ` string`The icon displayed next to the title.  
`close`| `false`| `boolean | Partial<ButtonProps>`Display a close button to dismiss the banner. `{ size: 'md', color: 'neutral', variant: 'ghost' }`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`target`| | ` null | "_blank" | "_parent" | "_self" | "_top" | string & {}`  
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Show properties

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

  
`title`| | ` string`  
`id`| `'1'`| ` string`A unique id saved to local storage to remember if the
banner has been dismissed. Change this value to show the banner again.  
`actions`| | ` ButtonProps[]`Display a list of actions next to the title. `{ color: 'neutral', size: 'xs' }`Show properties

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
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`closeIcon`| `appConfig.ui.icons.close`| ` string`The icon displayed in the
close button.  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; left?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; icon?: ClassNameValue; title?: ClassNameValue; actions?: ClassNameValue; close?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`title`| `{}`  
`actions`| `{}`  
`close`| `{ ui: any; }`  
  
### Emits

Event |  Type   
---|---  
`close`| `any[]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        banner: {
          slots: {
            root: [
              'relative z-50 w-full',
              'transition-colors'
            ],
            container: 'flex items-center justify-between gap-3 h-12',
            left: 'hidden lg:flex-1 lg:flex lg:items-center',
            center: 'flex items-center gap-1.5 min-w-0',
            right: 'lg:flex-1 flex items-center justify-end',
            icon: 'size-5 shrink-0 text-inverted pointer-events-none',
            title: 'text-sm text-inverted font-medium truncate',
            actions: 'flex gap-1.5 shrink-0 isolate',
            close: 'text-inverted hover:bg-default/10 focus-visible:bg-default/10 -me-1.5 lg:me-0'
          },
          variants: {
            color: {
              primary: {
                root: 'bg-primary'
              },
              secondary: {
                root: 'bg-secondary'
              },
              success: {
                root: 'bg-success'
              },
              info: {
                root: 'bg-info'
              },
              warning: {
                root: 'bg-warning'
              },
              error: {
                root: 'bg-error'
              },
              neutral: {
                root: 'bg-inverted'
              }
            },
            to: {
              true: ''
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              to: true,
              class: {
                root: 'hover:bg-primary/90'
              }
            },
            {
              color: 'neutral',
              to: true,
              class: {
                root: 'hover:bg-inverted/90'
              }
            }
          ],
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
          uiPro: {
            banner: {
              slots: {
                root: [
                  'relative z-50 w-full',
                  'transition-colors'
                ],
                container: 'flex items-center justify-between gap-3 h-12',
                left: 'hidden lg:flex-1 lg:flex lg:items-center',
                center: 'flex items-center gap-1.5 min-w-0',
                right: 'lg:flex-1 flex items-center justify-end',
                icon: 'size-5 shrink-0 text-inverted pointer-events-none',
                title: 'text-sm text-inverted font-medium truncate',
                actions: 'flex gap-1.5 shrink-0 isolate',
                close: 'text-inverted hover:bg-default/10 focus-visible:bg-default/10 -me-1.5 lg:me-0'
              },
              variants: {
                color: {
                  primary: {
                    root: 'bg-primary'
                  },
                  secondary: {
                    root: 'bg-secondary'
                  },
                  success: {
                    root: 'bg-success'
                  },
                  info: {
                    root: 'bg-info'
                  },
                  warning: {
                    root: 'bg-warning'
                  },
                  error: {
                    root: 'bg-error'
                  },
                  neutral: {
                    root: 'bg-inverted'
                  }
                },
                to: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  to: true,
                  class: {
                    root: 'hover:bg-primary/90'
                  }
                },
                {
                  color: 'neutral',
                  to: true,
                  class: {
                    root: 'hover:bg-inverted/90'
                  }
                }
              ],
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
          uiPro: {
            banner: {
              slots: {
                root: [
                  'relative z-50 w-full',
                  'transition-colors'
                ],
                container: 'flex items-center justify-between gap-3 h-12',
                left: 'hidden lg:flex-1 lg:flex lg:items-center',
                center: 'flex items-center gap-1.5 min-w-0',
                right: 'lg:flex-1 flex items-center justify-end',
                icon: 'size-5 shrink-0 text-inverted pointer-events-none',
                title: 'text-sm text-inverted font-medium truncate',
                actions: 'flex gap-1.5 shrink-0 isolate',
                close: 'text-inverted hover:bg-default/10 focus-visible:bg-default/10 -me-1.5 lg:me-0'
              },
              variants: {
                color: {
                  primary: {
                    root: 'bg-primary'
                  },
                  secondary: {
                    root: 'bg-secondary'
                  },
                  success: {
                    root: 'bg-success'
                  },
                  info: {
                    root: 'bg-info'
                  },
                  warning: {
                    root: 'bg-warning'
                  },
                  error: {
                    root: 'bg-error'
                  },
                  neutral: {
                    root: 'bg-inverted'
                  }
                },
                to: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  to: true,
                  class: {
                    root: 'hover:bg-primary/90'
                  }
                },
                {
                  color: 'neutral',
                  to: true,
                  class: {
                    root: 'hover:bg-inverted/90'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui-pro/blob/v3/src/theme/banner.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[BadgeA short text to represent a status or a
category.](/components/badge)[BlogPostA customizable article to display in a
blog page.](/components/blog-post)

